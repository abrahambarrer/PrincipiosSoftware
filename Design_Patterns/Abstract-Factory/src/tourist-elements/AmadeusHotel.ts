import { IHotel } from "../interfaces";

export class AmadeusHotel implements IHotel {
    name: string;
    geoCode: {latitude: number; longitude: number};
    address: {postalCode: string; lines: string[]};
    rating: number;
    lastUpdate: string;

    constructor(
        name: string,
        geoCode: {latitude: number; longitude: number},
        address: {postalCode: string; lines: string[]},
        rating: number,
        lastUpdate: string
    )
}