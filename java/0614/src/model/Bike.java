package model;

public class Bike extends Fulei {
	public Bike() {
		super("捷安特","蓝色");
	}
	
	public String info() {
		String str = "这是一辆"+this.getColor()+"颜色的,"+this.getBand()+"牌的自行车";
		return str;
	}
}
