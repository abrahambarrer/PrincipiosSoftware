import { IHotel } from "../interfaces";
import { Hotel } from "../types";

export class MockHotel implements IHotel {
    name: string;
    geoCode: {latitude: number; longitude: number };
    address: { postalCode: string; lines: string[]}
    rating: number;
    lastUpdate: string;

    constructor(hotelData: Hotel) {
        this.name 
    }
}