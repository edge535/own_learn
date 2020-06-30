package model;

public class Sanlun extends Fulei {
	public Sanlun() {
		super();
		super.setLunzi(3);
	}
	public String info() {
		String str = "三路车是一款有"+super.getLunzi()+"个轮子的非机动车";
		return str;
	}
}
