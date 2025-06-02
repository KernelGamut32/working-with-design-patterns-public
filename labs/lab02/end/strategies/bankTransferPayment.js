// strategies/bankTransferPayment.js

class BankTransferPayment {
  /**
   * @param {object} data 
   *   - accountNumber: string
   *   - routingNumber: string
   *   - amount: number
   */
  constructor(data) {
    this.accountNumber = data.accountNumber;
    this.routingNumber = data.routingNumber;
    this.amount        = data.amount;
  }

  /**
   * Processes a bank transfer payment.
   * @returns {Promise<string>}
   */
  async process() {
    console.log("Initiating bank transfer...");
    await this._fakeNetworkLatency();
    console.log(`Transferring $${this.amount} from account ${this.accountNumber}`);
    await this._fakeNetworkLatency();
    return `BankTransfer of $${this.amount} succeeded.`;
  }

  async _fakeNetworkLatency() {
    return new Promise(res => setTimeout(res, 300));
  }
}

module.exports = BankTransferPayment;
