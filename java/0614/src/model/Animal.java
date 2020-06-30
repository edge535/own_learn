package model;

public class Animal {
	private String name;
	private int month;
	
	public Animal() {}
	public Animal(String name, int month) {
		this.name = name;
		this.month = month;
	}
	protected String getName() {
		return name;
	}
	protected void setName(String name) {
		this.name = name;
	}
	protected int getMonth() {
		return month;
	}
	protected void setMonth(int month) {
		this.month = month;
	}
	
	
	public void eat() {
		System.out.println("动物都有吃东西的能力");
	}
}
