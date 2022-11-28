package day02;

public class OopTest {
	public static void main(String[] args) {
//		Animal animal = new Animal();
//		System.out.println(animal.age);
//		animal.getOlder();
//		System.out.println(animal.age);
		
		Human hum = new Human();
		System.out.println(hum.age);
		System.out.println(hum.language);
		hum.getOlder();
		hum.momstouch(7);
		System.out.println(hum.age);
		System.out.println(hum.language);
	}
}
