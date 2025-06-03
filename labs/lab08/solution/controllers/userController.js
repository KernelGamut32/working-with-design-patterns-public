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
