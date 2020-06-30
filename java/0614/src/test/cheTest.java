package test;
import model.*;

public class cheTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Fulei fulei = new Fulei();
		Bike bike = new Bike();
		Elebike elebike = new Elebike("BYD");
		Sanlun sanlun = new Sanlun();
		System.out.println(fulei.info());
		System.out.println(bike.info());
		System.out.println(elebike.info());
		System.out.println(sanlun.info());
	}

}
