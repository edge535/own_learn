package model;

public class Dog extends Animal {
	private String sex;
	
	public Dog() {}
	public Dog(String name, int month, String sex) {
		this.setName(name);
		this.setMonth(month);
		this.sex = sex;
	}
	protected String getSex() {
		return sex;
	}
	protected void setSex(String sex) {
		this.sex = sex;
	}
	
	public void sleep() {
		System.out.println("小狗有午睡的习惯");
	}
	
	@Override
	public void eat() {
		// TODO Auto-generated method stub
		System.out.println("狗吃肉");
	}
}
