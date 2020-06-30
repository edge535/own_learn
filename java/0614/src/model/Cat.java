package model;

public class Cat extends Animal {
	private double weight;
	
	public Cat() {}
	public Cat(String name, int month, double weight) {
		super(name,month);
		this.weight = weight;
	}
	
	protected double getWeight() {
		return weight;
	}
	protected void setWeight(double weight) {
		this.weight = weight;
	}
	
	public void run() {
		System.out.println("小猫快乐的奔跑");
	}
	
	@Override
	public void eat() {
		// TODO Auto-generated method stub
		System.out.println("猫吃鱼");
	}
}
