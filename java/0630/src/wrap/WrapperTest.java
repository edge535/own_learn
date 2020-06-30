package wrap;

public class WrapperTest {

	public static void main(String[] args) {
		Integer one = new Integer(100);
		Integer two = new Integer(100);
		System.out.println("one == two : "+(one == two));
		
		Integer three = 100;
		System.out.println("three == 100 : "+(three == 100));
		
		Integer four = 100;
		System.out.println("three == four : "+(three == four));
		
		Integer five = 200;
		System.out.println("five == 200 : "+(five == 200));
		
		Integer six = 200;
		System.out.println("five == six : "+(five == six));
	}
	
}
