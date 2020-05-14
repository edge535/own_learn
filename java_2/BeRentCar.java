package test.jv2;

public class BeRentCar extends RentCar {
	public BeRentCar(int nameindex, int rentcost, int seatcount, int transportcount) {
		super(nameindex, rentcost, seatcount, transportcount);
	}

	public String[] getElement(){
		String[] element = {this.name, this.rentCost+"", this.seatCount+"", this.transportCount+""};
		return element;
	}
	
	
//	public static void main(String[] args) {
//		BeRentCar car = new BeRentCar(1, 500, 4, 0);
//		String[] element = car.getElement();
//		for(String ele : element) {
//			System.out.println(ele);
//		}
//	}
	
	
	
}
