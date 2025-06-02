// index.js

const PaymentProcessor = require("./paymentProcessor");

async function main() {
  const processor = new PaymentProcessor();

  try {
    // Example 1: Credit Card payment
    const ccResult = await processor.processPayment("CreditCard", {
      cardNumber: "4111 1111 1111 1111",
      expiry: "12/25",
      cvv: "123",
      amount: 75.00,
    });
    console.log(ccResult);
    console.log("------------------------------");

    // Example 2: PayPal payment
    const ppResult = await processor.processPayment("PayPal", {
      email: "alice@example.com",
      password: "s3cr3t!",
      amount: 42.50,
    });
    console.log(ppResult);
    console.log("------------------------------");

    // Example 3: Bank Transfer payment
    const btResult = await processor.processPayment("BankTransfer", {
      accountNumber: "123456789",
      routingNumber: "987654321",
      amount: 120.00,
    });
    console.log(btResult);
    console.log("------------------------------");

    // Example 4: Unsupported payment type
    await processor.processPayment("Bitcoin", {
      walletAddress: "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
      amount: 0.005,
    });
  } catch (err) {
    console.error("Error:", err.message);
  }
}

main();
