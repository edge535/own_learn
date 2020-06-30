package test;
import model.Animal;
import model.Cat;
import model.Dog;

public class animalTest {
	public static void main(String[] args) {
		Animal one = new Animal();
		Animal two = new Cat();
		Animal three = new Dog();
		
		one.eat();
		two.eat();
		three.eat();
		
		System.out.println("============================");
		Cat temp = (Cat)two;
		temp.eat();
		temp.run();
	}
}
