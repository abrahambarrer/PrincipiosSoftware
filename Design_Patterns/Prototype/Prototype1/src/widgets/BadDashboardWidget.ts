import { ThemeManager } from "../core/ThemeManager";
import { ChartEngine } from "../core/ChartEngine";
import { DataCache } from "../core/DataCache";

export class BadDashboardWidget {
    constructor {
        private title: string,
        private type: string, 
        private theme: any,
        private chartEngine: ChartEngine,
        private dataCache: any
    } {}

    static async create(title: string, type: string) {
        console.time("Crear widget (Sin prototype)");

        const theme = await ThemeManager.load();

        const chartEngine = new ChartEngine();
        await chartEngine.initialize();

        const dataCache = new DataCache().load();

        console.timeEnd("Crear widget (Sin prototype)");

        return new BadDashboardWidget();
    }

    render(container: HTMLElement, index: number) {
        const widget = document.createElement("div";
            widget.className = "widget";

            const coloer = this.theme.palette[(index * 10) % this.theme.palette.length];

            widget.innerHTML = `<h3>${this.title} #${index + 1}</h3><canvas></canvas>`;
            container.appendChild(widget);

            const canvas = widget.querySelector
        )
    }
}