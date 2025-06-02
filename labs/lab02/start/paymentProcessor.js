// paymentProcessor.js

class PaymentProcessor {
  /**
   * Processes a payment based on the given type.
   * 
   * @param {string} type    - The payment method type (e.g., "CreditCard", "PayPal").
   * @param {object} data    - Payment data specific to each type.
   * @returns {Promise<string>} - A Promise resolving to a success message.
   */
  async processPayment(type, data) {
    if (type === "CreditCard") {
      return this._processCreditCard(data);
    } else if (type === "PayPal") {
      return this._processPayPal(data);
    } else if (type === "BankTransfer") {
      return this._processBankTransfer(data);
    } else {
      throw new Error(`Unsupported payment type: ${type}`);
    }
  }

  async _processCreditCard({ cardNumber, expiry, cvv, amount }) {
    // (Imaginary) steps to process a credit‐card transaction
    console.log("Validating credit card details...");
    await this._fakeNetworkLatency();
    console.log(`Charging $${amount} to credit card ${cardNumber} (exp ${expiry})`);
    await this._fakeNetworkLatency();
    return `CreditCard payment of $${amount} succeeded.`;
  }

  async _processPayPal({ email, password, amount }) {
    console.log("Authenticating with PayPal...");
    await this._fakeNetworkLatency();
    console.log(`Sending $${amount} from PayPal account ${email}`);
    await this._fakeNetworkLatency();
    return `PayPal payment of $${amount} succeeded.`;
  }

  async _processBankTransfer({ accountNumber, routingNumber, amount }) {
    console.log("Initiating bank transfer...");
    await this._fakeNetworkLatency();
    console.log(`Transferring $${amount} from account ${accountNumber}`);
    await this._fakeNetworkLatency();
    return `BankTransfer of $${amount} succeeded.`;
  }

  async _fakeNetworkLatency() {
    return new Promise(res => setTimeout(res, 300));
  }
}

module.exports = PaymentProcessor;
