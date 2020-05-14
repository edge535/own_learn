package test.jv2;

public abstract class RentCar {
	public String name;
	public int nameIndex;
	public int rentCost;
	public int seatCount;
	public int transportCount;

	public abstract String[] getElement();
	
	public RentCar() {
		this.name = "test";
		this.nameIndex = -1;
		this.rentCost = -1;
		this.seatCount = -1;
		this.transportCount = -1;
	}
	
	public RentCar(int nameindex, int rentcost, int seatcount, int transportcount) {
		RentCarName carname = new RentCarName();
		this.name = carname.getName(nameindex);
		this.nameIndex = nameindex;
		this.rentCost = rentcost;
		this.seatCount = seatcount;
		this.transportCount = transportcount != 0 ? transportcount : 0;
	}

//	public static void main(String[] args) {
//		RentCar r = new RentCar();
//		String[] ele = r.getElement();
//		System.out.println(ele[0]);
//		System.out.println(ele[1]);
//		System.out.println(ele[2]);
//	}
	
	
}