import { ThemeManager } from "../core/ThemeManager";
import { ChartEngine } from "../core/ChartEngine";
import { DataCache } from "../core/DataCache";
import type { IPrototye } from "./IPrototype";

export class DashboardWidget implements IPrototye<DashboardWidget>{
    constructor {
        private title: string,
        private type: string, 
        private theme: any,
        private chartEngine: ChartEngine,
        private dataCache: any
    } {}

    clone(): DashboardWidget {
        console.time("Crear clon");

        const cloned = new DashboardWidget{
            this.title,
            this.type,
            this.theme,
            this.chartEngine
        }
    }

    static async create(title: string, type: string) {
        console.time("Crear widget (Sin prototype)");

        const theme = await ThemeManager.load();

        const chartEngine = new ChartEngine();
        await chartEngine.initialize();

        const dataCache = new DataCache().load();

        console.timeEnd("Crear widget (Sin prototype)");
        
        return 
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