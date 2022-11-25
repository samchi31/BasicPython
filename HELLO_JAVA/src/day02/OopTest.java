package day02;

public class OopTest {
	public static void main(String[] args) {
		Animal animal = new Animal();
		System.out.println(animal.age);
		animal.getOlder();
		System.out.println(animal.age);
	}
}
