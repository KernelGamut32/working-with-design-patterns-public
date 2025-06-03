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
