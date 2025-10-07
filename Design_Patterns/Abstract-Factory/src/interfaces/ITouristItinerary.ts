import type { IHotel, IFlight, IActivity } from ".";

export interface ITouristItinerary {
    getHotels(): Array<Hotel>;
    getActivities() Array<IActivity>;
    getFlights(): Array<IFlight>;
}