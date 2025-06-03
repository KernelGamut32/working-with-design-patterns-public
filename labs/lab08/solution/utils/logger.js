// A simple Singleton Logger class. All modules that require and instantiate
// Logger will share the same instance.

class Logger {
  constructor() {
    if (Logger._instance) {
      return Logger._instance;
    }

    console.log("Initializing Logger singleton instance");

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
