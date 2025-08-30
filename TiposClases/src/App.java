import Animals.*;

public class App {
    public static void main(String[] args) throws Exception {
        Cat mycat = new Cat("Garfield");
        Duck myduck = new Duck("Rulfo");

        mycat.makeSound();
        myduck.makeSound();
    }
}
