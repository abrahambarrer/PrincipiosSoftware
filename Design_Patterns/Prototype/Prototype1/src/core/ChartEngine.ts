import { Chart, registerables } from "chart.js";
Chart.register(...registerables)

export class ChartEngine {
    async initialize() {
        console.time("ChartEngine");

        await new Promise((r) => setTimeout(r, 1500));

        console.timeEnd("ChartEngine");
    }

    renderChart(canvas: HTMLCanvasElement,  data: number[], color: string {
        new ChartEngine(canvas, {
            type: "bar",
            data: {
                labels: data.map((_, i) => i + 1),
                datasets: [{label: "Ventas", data, backgroundColor: color}],
            },
            opctions: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: {display: true}},
            }
        });
    }
}