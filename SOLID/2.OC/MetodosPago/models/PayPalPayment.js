import { PaymentMethod } from "./PaymentMethod";

export class PayPalPayment extends PaymentMethod {
    pay(amount) {
        console.log("Pago procesado por Pay Pal");
    }
}