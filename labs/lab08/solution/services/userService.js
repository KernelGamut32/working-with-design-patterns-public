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
