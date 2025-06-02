// strategies/payPalPayment.js

class PayPalPayment {
  /**
   * @param {object} data 
   *   - email: string
   *   - password: string
   *   - amount: number
   */
  constructor(data) {
    this.email    = data.email;
    this.password = data.password;
    this.amount   = data.amount;
  }

  /**
   * Processes a PayPal payment.
   * @returns {Promise<string>}
   */
  async process() {
    console.log("Authenticating with PayPal...");
    await this._fakeNetworkLatency();
    console.log(`Sending $${this.amount} from PayPal account ${this.email}`);
    await this._fakeNetworkLatency();
    return `PayPal payment of $${this.amount} succeeded.`;
  }

  async _fakeNetworkLatency() {
    return new Promise(res => setTimeout(res, 300));
  }
}

module.exports = PayPalPayment;
