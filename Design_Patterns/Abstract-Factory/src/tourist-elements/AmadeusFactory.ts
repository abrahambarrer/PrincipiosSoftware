import type { ITouristItinerary } from "../interfaces/ITouristItinerary";
import { AmadeusHotel } from "./AmadeusHotel";

export class AmadeusFactory implements ITouristItinerary {
    async getHotels(): Array<IHotek> {
        const hotels = await baseRequest<Hotel>(
            authToken,
            getHotelsEndpoint(cityCode)
        );

        return hotels.map(hotels: Hotel) => new AmadeusHotel(hotel).getData();
    };
    async getActivities(): Promise<Array<IActivity>> {
        const acitivities = await baseRequest<Activity> {
            authToken,
            getActivitiesEndpoint(cityCode)
        }
        return [];
    };
}