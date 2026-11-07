// Ошибка компиляции
// 1. makeSound(int numberOfSounds) не определён в Animal -- нечего переопределять
// 2. Вызов cat.makeSound(3) невозможен, так как makeSound(int numberOfSounds) не определён в Animal

class Animal {
    public void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

class Cat extends Animal {
    @Override
    public void makeSound(int numberOfSounds) {
        for (int i = 0; i < numberOfSounds; i++) {
            System.out.println("Meow");
        }
    }
    
    @Override
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal cat = new Cat();
        cat.makeSound();
        cat.makeSound(3);
    }
}