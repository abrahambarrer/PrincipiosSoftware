package Animals;

public class Cat extends Animal {
    String name;

    public Cat(String name) {
        this.name = name;
    }

    @Override
    public void makeSound() {
        System.out.println(name + " says Meow");
    }
}
