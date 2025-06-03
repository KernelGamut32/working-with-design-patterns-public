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
