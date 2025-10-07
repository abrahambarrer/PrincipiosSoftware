export class MockActivity implements IActivity {
    type: string;
    name: string;
    price: {
        amount: string,
        currencyCode: string
    }
}