package exportadorreportes;

public class ReportService {
    private final CsvExportable csv;

    public ReportService(CsvExportable csv) {
        this.csv = csv;
    }

    public void exportarVentas(String data) {
        csv.exportCsv(data);
    }
}
