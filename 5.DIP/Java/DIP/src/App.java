import mal_ejemplo.ServicioNoti;
import buen_ejemplo.*;

public class App {
    public static void main(String[] args) throws Exception {
        // Mal ejemplo
        ServicioNoti servicionoti = new ServicioNoti();
        servicionoti.enviar("Hola Mundo");

        // Buen ejemplo
        Notificador email = new Email();
        Notificador sms = new Sms();
        Notificador whatsapp = new WhatsApp();

        ServicioNotificador ServicioEmail = new ServicioNotificador(email);
        ServicioNotificador Serviciosms = new ServicioNotificador(sms);
        ServicioNotificador Serviciowhatsapp = new ServicioNotificador(whatsapp);

        ServicioEmail.notificar("Hola");
        Serviciosms.notificar("Hola sms");
        Serviciowhatsapp.notificar("Hola whatsapp");
    }
}
