package Animals;

public class Duck extends Animal implements Flyer{
    String name;

    public Duck(String name) {
        this.name = name;
    }

    @Override
    public void makeSound() {
        System.out.println(name + " says cuak...");
    }

    @Override
    public void fly() {
        System.out.println(name + " is flying...");
    }
    
}
