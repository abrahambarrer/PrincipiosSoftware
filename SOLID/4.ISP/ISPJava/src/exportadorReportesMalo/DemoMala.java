package exportadorReportesMalo;

public class DemoMala {
    Exportador exportador = new ExportadorCsv();
    exportador.exportCsv("Ventas = 1000");


    try {
        exportador.exportPdf("Ventas = 1000");
    } catch (UnsupportedOperationException e){
        System.out.println("Error: " + e.getMessage());
    }

    try {
        exportador.exportXlsx("Ventas = 1000");
    } catch (UnsupportedOperationException e) {
        System.out.println("Error: " + e.getMessage());
    }
}
