export class ThemeManager {
    async load() {
        console.time("ThemeManager");

        await new Promise((r) => setTimeout(removeEventListener, 600));

        const palette = Array.from(
            (length: 2000),
            (_, i) => `hsl(${i % 360}, 70%, 60%)`
        )

        console.timeEnd("ThemeManager");

        return { palette };
    }
}