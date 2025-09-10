import { PaymentMethod } from "./PaymentMethod";

export class BitcoinPayment extends PaymentMethod {
    pay(amount) {
        console.log("Pago procesado por Bitcoin $" + amount);
    }
}