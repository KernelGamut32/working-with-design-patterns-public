# Lab 08 - Singleton Pattern

## Overview

In this lab, you will build and explore a Node.js application that demonstrates the Singleton pattern in software engineering. You’ll create a simple Express-based REST API that includes:

- A **Singleton Logger** for centralized logging
- A **Singleton In-Memory Database** for storing user records
- A **UserService** layer that interacts with the database
- A **UserController** layer that maps HTTP routes to service methods
- A **server.js** entry point that ties everything together

By the end of this lab, you will understand how and why the Singleton pattern ensures only one instance of certain classes (e.g., Logger, Database) is created and shared across the entire application.

---

## Learning Objectives

- Understand the purpose and structure of the Singleton pattern
- Implement a Singleton class in JavaScript/Node.js
- Wire multiple modules to share a single instance of a Logger and Database
- Build a minimal Express-based REST API that uses these singletons
- Verify singleton behavior through hands-on testing
- Reflect on scenarios where the Singleton pattern is appropriate

---

## Prerequisites

Before starting this lab, ensure you have:

1. **Node.js (v14+)** and **npm** installed.
2. A code editor (e.g., VS Code, WebStorm, Sublime).
3. Basic familiarity with:
   - JavaScript/Node.js syntax
   - `npm init`, `npm install`
   - Express routing (`express.Router`)
   - ES5/ES6 module exports (`module.exports`, `require`)
4. cURL or Postman (or another HTTP client) to test the REST endpoints.

---

## Lab Setup

1. Open a terminal, create a new directory for the lab, and initialize the Node project:

```bash
mkdir singleton-example
cd singleton-example
```

2. Initialize a new `package.json`:

```bash
npm init -y
```

3. Install dependencies:

```bash
npm install express uuid --save
npm install --save-dev nodemon
```

- `express`: For HTTP routing
- `uuid`: To generate unique IDs for users
- `nodemon` (dev-dependency): Automatically restarts the server on file changes

4. Update `package.json` to add start scripts. Open `package.json` and modify the `"scripts"` section so it looks like this:

```json
"scripts": {
  "start": "node server.js",
  "dev": "nodemon server.js"
}
```

- `npm start` will run `node server.js`
- `npm run dev` with run `nodemon server.js`, which reloads on file changes

---

## Repository Structure

Place the following six files in a directory named `singleton-example/`:

```text
singleton-example/
├── package.json
├── server.js
├── controllers/
│   └── userController.js
├── services/
│   └── userService.js
├── db/
│   └── database.js
└── utils/
    └── logger.js
```

Below is a brief summary of each file’s purpose:

- **server.js:** Entry point for Express server
- **controllers/userController.js:** Defines HTTP routes for `/users`
- **services/userService.js:** Contains business logic for user CRUD
- **db/database.js:** In-memory Database singleton
- **utils/logger.js:** Logger singleton

---

## Examine the Code

utils/logger.js

```javascript
// A simple Singleton Logger class. All modules that require and instantiate
// Logger will share the same instance.

class Logger {
  constructor() {
    if (Logger._instance) {
      return Logger._instance;
    }

    // Define log levels
    this.levels = { DEBUG: 0, INFO: 1, WARN: 2, ERROR: 3 };
    this.currentLevel = this.levels.DEBUG;

    Logger._instance = this;
  }

  setLevel(levelName) {
    if (this.levels[levelName] !== undefined) {
      this.currentLevel = this.levels[levelName];
    } else {
      this.error(`Invalid log level: ${levelName}`);
    }
  }

  log(levelName, message) {
    const levelValue = this.levels[levelName];
    if (levelValue === undefined) {
      console.error(`[Logger] Invalid level: ${levelName}`);
      return;
    }
    if (levelValue >= this.currentLevel) {
      const timestamp = new Date().toISOString();
      console.log(`[${timestamp}] [${levelName}] ${message}`);
    }
  }

  debug(msg) {
    this.log("DEBUG", msg);
  }

  info(msg) {
    this.log("INFO", msg);
  }

  warn(msg) {
    this.log("WARN", msg);
  }

  error(msg) {
    this.log("ERROR", msg);
  }
}

module.exports = Logger;
```

db/database.js

```javascript
// A mock Singleton “Database” using an in-memory object. All modules that
// require and instantiate Database will share the same data store.

const { v4: uuidv4 } = require("uuid");
const Logger = require("../utils/logger");

class Database {
  constructor() {
    if (Database._instance) {
      return Database._instance;
    }

    this._logger = new Logger();
    this._logger.info("Initializing Database singleton instance");

    // In-memory “table” of users (keyed by ID)
    this.users = {};

    Database._instance = this;
  }

  createUser({ name, email }) {
    const id = uuidv4();
    const newUser = {
      id,
      name,
      email,
      createdAt: new Date().toISOString(),
    };
    this.users[id] = newUser;
    this._logger.debug(`User created with ID: ${id}`);
    return newUser;
  }

  getUserById(id) {
    const user = this.users[id] || null;
    if (user) {
      this._logger.debug(`Retrieved user: ${id}`);
    } else {
      this._logger.warn(`User not found: ${id}`);
    }
    return user;
  }

  updateUser(id, { name, email }) {
    const user = this.users[id];
    if (!user) {
      this._logger.warn(`Cannot update, user not found: ${id}`);
      return null;
    }
    if (name !== undefined) user.name = name;
    if (email !== undefined) user.email = email;
    user.updatedAt = new Date().toISOString();
    this._logger.debug(`User updated: ${id}`);
    return user;
  }

  deleteUser(id) {
    if (!this.users[id]) {
      this._logger.warn(`Cannot delete, user not found: ${id}`);
      return false;
    }
    delete this.users[id];
    this._logger.debug(`User deleted: ${id}`);
    return true;
  }

  listUsers() {
    this._logger.debug("Listing all users");
    return Object.values(this.users);
  }
}

module.exports = Database;
```

services/userService.js

```javascript
// Contains business logic for user CRUD. Uses the Database singleton.

const Database = require("../db/database");
const Logger = require("../utils/logger");

class UserService {
  constructor() {
    this._db = new Database();
    this._logger = new Logger();
    this._logger.info("UserService instantiated");
  }

  createUser(data) {
    this._logger.info("UserService: createUser called");
    return this._db.createUser(data);
  }

  getUser(id) {
    this._logger.info(`UserService: getUser called for ID ${id}`);
    return this._db.getUserById(id);
  }

  updateUser(id, data) {
    this._logger.info(`UserService: updateUser called for ID ${id}`);
    return this._db.updateUser(id, data);
  }

  deleteUser(id) {
    this._logger.info(`UserService: deleteUser called for ID ${id}`);
    return this._db.deleteUser(id);
  }

  listUsers() {
    this._logger.info("UserService: listUsers called");
    return this._db.listUsers();
  }
}

module.exports = UserService;
```

controllers/userController.js

```javascript
// Maps HTTP routes to UserService methods. Uses the Logger singleton.

const express = require("express");
const UserService = require("../services/userService");
const Logger = require("../utils/logger");

const router = express.Router();
const userService = new UserService();
const logger = new Logger();

// GET /users      - List all users
// POST /users     - Create a new user
// GET /users/:id  - Retrieve a specific user
// PUT /users/:id  - Update a user
// DELETE /users/:id - Delete a user

// List users
router.get("/", (req, res) => {
  logger.info("GET /users");
  const users = userService.listUsers();
  res.json(users);
});

// Create user
router.post("/", (req, res) => {
  logger.info("POST /users");
  const { name, email } = req.body;
  if (!name || !email) {
    logger.warn("POST /users: missing name or email");
    return res.status(400).json({ error: "name and email are required" });
  }
  const created = userService.createUser({ name, email });
  res.status(201).json(created);
});

// Get user by ID
router.get("/:id", (req, res) => {
  const { id } = req.params;
  logger.info(`GET /users/${id}`);
  const user = userService.getUser(id);
  if (!user) {
    return res.status(404).json({ error: "User not found" });
  }
  res.json(user);
});

// Update user by ID
router.put("/:id", (req, res) => {
  const { id } = req.params;
  const { name, email } = req.body;
  logger.info(`PUT /users/${id}`);
  const updated = userService.updateUser(id, { name, email });
  if (!updated) {
    return res.status(404).json({ error: "User not found" });
  }
  res.json(updated);
});

// Delete user by ID
router.delete("/:id", (req, res) => {
  const { id } = req.params;
  logger.info(`DELETE /users/${id}`);
  const deleted = userService.deleteUser(id);
  if (!deleted) {
    return res.status(404).json({ error: "User not found" });
  }
  res.status(204).send();
});

module.exports = router;
```

server.js

```javascript
// Main entry point: sets up Express, JSON body parsing, and routes.

const express = require("express");
const bodyParser = require("body-parser");
const userController = require("./controllers/userController");
const Logger = require("./utils/logger");

const app = express();
const logger = new Logger();

// Set logging level to DEBUG (so all log messages are printed)
logger.setLevel("DEBUG");

app.use(bodyParser.json());

// Health check endpoint
app.get("/health", (req, res) => {
  logger.info("GET /health");
  res.json({ status: "UP", timestamp: new Date().toISOString() });
});

// Mount the UserController at /users
app.use("/users", userController);

// 404 handler
app.use((req, res) => {
  logger.warn(`Unknown route: ${req.method} ${req.originalUrl}`);
  res.status(404).json({ error: "Not Found" });
});

// Error handler
app.use((err, req, res, next) => {
  logger.error(`Error encountered: ${err.message}`);
  res.status(500).json({ error: "Internal Server Error" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  logger.info(`Server started on port ${PORT}`);
});
```

## Run and Test the Application

- Use either `npm start` or `npm run dev` to launch the application.
- Verify the `/health` endpoing using `curl http://localhost:3000/health` You should see the following JSON output:

```json
{
  "status": "UP",
  "timestamp": "2025-06-03TXX:XX:XX.ZZZZ"
}
```

- Create a user:

```bash
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'
```

Expected response

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Alice",
  "email": "alice@example.com",
  "createdAt": "2025-06-03TXX:XX:XX.ZZZZ"
}
```

- List users:

```bash
curl http://localhost:3000/users
```

Expected response

```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "Alice",
    "email": "alice@example.com",
    "createdAt": "2025-06-03TXX:XX:XX.ZZZZ"
  }
]
```

- Get a user by ID:

```bash
curl http://localhost:3000/users/550e8400-e29b-41d4-a716-446655440000
```

- Update a user:

```bash
curl -X PUT \
    http://localhost:3000/users/550e8400-e29b-41d4-a716-446655440000 \
    -H "Content-Type: application/json" \
    -d '{"name":"Alice Smith"}'
```

- Delete a user:

```bash
curl -X DELETE http://localhost:3000/users/550e8400-e29b-41d4-a716-446655440000
```
