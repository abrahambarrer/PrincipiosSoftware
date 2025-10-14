export class DataCache {
    load() {
        console.time("DataCache");

        const data = Array.from({length: 50}, () => {
            ventas: Math.floor(Math.random() * 100)
        })

        console.timeEnd("DataCache");

        return data;
    }
}