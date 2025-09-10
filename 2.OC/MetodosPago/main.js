import { PaymentService } from "./services/PaymentServices";
import { CreditCardPayment } from "./models/CreditCardPayment";
import { PayPalPayment } from "./models/PayPalPayment";
import { BitcoinPayment } from "./models/BitcoinPayment";

const service = new PaymentService();

const creditCart = new CreditCardPayment();
const paypalPayment = new PayPalPayment();
const bictoinPayment = new BitcoinPayment();

service.serviceProcess(creditCart, 200);
service.serviceProcess(paypalPayment, 300);
service.serviceProcess(bictoinPayment, 1000);