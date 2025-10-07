itineraries: {
    duration: string;
    segments: {
        from: string;
        duration: string;
        stops?: {
            iataCode: string;
            duration: string;
            arrivalAt: string
        }
    }
}