// paymentProcessor.js

class PaymentProcessor {
  /**
   * @param {object} strategyInstance
   *   - Must have a method `async process() -> Promise<string>`
   */
  constructor(strategyInstance) {
    if (!strategyInstance || typeof strategyInstance.process !== "function") {
      throw new Error("A valid strategy instance with a process() method is required.");
    }
    this._strategy = strategyInstance;
  }

  /**
   * Delegates processing to the injected strategy.
   * @returns {Promise<string>}
   */
  async process() {
    return this._strategy.process();
  }
}

module.exports = PaymentProcessor;
