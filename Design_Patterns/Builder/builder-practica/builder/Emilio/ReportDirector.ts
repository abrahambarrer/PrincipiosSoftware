import { ReportBuilder } from "./ReportBuilder";

export class ReportDirector {
    public async constructReport(builder: ReportBuilder): Promise <void> {
        await (builder as any).buildEncabezado();
        await (builder as any).buildCuerpo();
        await (builder as any).buildPieDePagina();
    }
}