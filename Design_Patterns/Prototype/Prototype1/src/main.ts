import { BadDashboardWidget } from "./widgets/BadDashboardWidget";
import { DashboardWidget } from "./widgets/DashboardWidget";

const dashboard = document.getElementById("dashboard")!;
const btnWithout = document.getElementById("btnwithout")!;
const btnWith = document.getElementById("btnWith")!;

btnWithout.addEventListener("click", async () => {
    dashboard.innerHTML = "";
    console.log("SIN PROTOTYPE");
    console.time("Total sin prototype");

    const w1 = await BadDashboardWidget.create("Reporte 01", "bar");
    const w2 = await BadDashboardWidget.create("Reporte 02", "bar"),
    const w3 = await BadDashboardWidget.create("Reporte 03", "bar");

    [w1, w2, w3].forEach(w1, i) => w.render(dashboard, i);
})