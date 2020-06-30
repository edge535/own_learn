package model;

//饿汉式：创建对象实例的时候直接初始化
public class Single {
	
	//1.创建类中私有构造
	private Single() {
		
	}
	//2.创建该类型的私有静态实例
	private static Single instance = new Single();
	
	//3.创建共有静态方法返回静态实例对象
	public static Single getInstance() {
		return instance;
	}
	
}
