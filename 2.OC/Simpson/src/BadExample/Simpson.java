package BadExample;

public class Simpson {
    String name;
}

public class Simpson(String name) {
    public static void hablar(Caricatura personaje) {
        switch (personaje.name) {
            case "Homero":
                System.out.println("D'oh!");
                break;
            case "Bart":
                System.out.println("Ay, caramba!");
                break;
            default:
                System.out.println("Personaje incorrecto");
                break;
        }
    }
}