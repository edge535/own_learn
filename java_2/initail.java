package test.jv2;

public class initail {
	public static void main(String[] args) {
		animal aanimal = new animal();
		System.out.println(aanimal.age);
		dog adog = new dog();
		adog.age = 3;
		adog.name = "Tom";
		adog.eat();
		System.out.println(adog);
	}
}
