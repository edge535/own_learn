package test;
import model.Single;
import model.SingleTwo;

public class singleTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Single one = Single.getInstance();
		Single two = Single.getInstance();
		System.out.println(one);
		System.out.println(two);
		
		System.out.println("==============================");
		SingleTwo one1 = SingleTwo.getInstance();
		SingleTwo two1 = SingleTwo.getInstance();
		System.out.println(one1);
		System.out.println(two1);
	}

}
