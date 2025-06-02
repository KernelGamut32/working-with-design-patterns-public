// index.js

const PaymentProcessor   = require("./paymentProcessor");
const CreditCardPayment  = require("./strategies/creditCardPayment");
const PayPalPayment      = require("./strategies/payPalPayment");
const BankTransferPayment = require("./strategies/bankTransferPayment");

async function main() {
  try {
    // 1) Credit Card
    const ccStrategy = new CreditCardPayment({
      cardNumber: "4111 1111 1111 1111",
      expiry: "12/25",
      cvv: "123",
      amount: 75.00,
    });
    const ccProcessor = new PaymentProcessor(ccStrategy);
    const ccResult = await ccProcessor.process();
    console.log(ccResult);
    console.log("------------------------------");

    // 2) PayPal
    const ppStrategy = new PayPalPayment({
      email: "alice@example.com",
      password: "s3cr3t!",
      amount: 42.50,
    });
    const ppProcessor = new PaymentProcessor(ppStrategy);
    const ppResult = await ppProcessor.process();
    console.log(ppResult);
    console.log("------------------------------");

    // 3) Bank Transfer
    const btStrategy = new BankTransferPayment({
      accountNumber: "123456789",
      routingNumber: "987654321",
      amount: 120.00,
    });
    const btProcessor = new PaymentProcessor(btStrategy);
    const btResult = await btProcessor.process();
    console.log(btResult);
    console.log("------------------------------");

    // 4) (If we wanted to add Bitcoin, we’d create
    //    strategies/bitcoinPayment.js and do:)
    //
    // const BitcoinPayment = require("./strategies/bitcoinPayment");
    // const btcStrategy = new BitcoinPayment({ walletAddress: "...", amount: 0.005 });
    // const btcProcessor = new PaymentProcessor(btcStrategy);
    // const btcResult = await btcProcessor.process();
    // console.log(btcResult);

  } catch (err) {
    console.error("Error:", err.message);
  }
}

main();
