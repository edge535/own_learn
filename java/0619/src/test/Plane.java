package test;


public class Plane implements Ifly {

	public void te() {
		System.out.println("测试自己的方法能不能被自己的实例和接口实例调用");
	}
	
	@Override
	public void fly() {
		// TODO Auto-generated method stub
		Ifly.super.fly();
		System.out.println("飞机在天上飞");
	}

	
	public static void main(String[] args) {
		Plane p1 = new Plane();
		p1.fly();
		p1.te();
		
		Ifly i1 = new Plane();
		i1.fly();
		
		Ifly.fly2();
	}
}
