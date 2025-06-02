// strategies/creditCardPayment.js

class CreditCardPayment {
  /**
   * @param {object} data 
   *   - cardNumber: string
   *   - expiry: string
   *   - cvv: string
   *   - amount: number
   */
  constructor(data) {
    this.cardNumber = data.cardNumber;
    this.expiry     = data.expiry;
    this.cvv        = data.cvv;
    this.amount     = data.amount;
  }

  /**
   * Processes a credit‐card payment.
   * @returns {Promise<string>}
   */
  async process() {
    console.log("Validating credit card details...");
    await this._fakeNetworkLatency();
    console.log(`Charging $${this.amount} to credit card ${this.cardNumber} (exp ${this.expiry})`);
    await this._fakeNetworkLatency();
    return `CreditCard payment of $${this.amount} succeeded.`;
  }

  async _fakeNetworkLatency() {
    return new Promise(res => setTimeout(res, 300));
  }
}

module.exports = CreditCardPayment;
