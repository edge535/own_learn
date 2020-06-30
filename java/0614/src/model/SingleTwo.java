package model;

//懒汉式：只有在第一次调用时才进行初始化，
public class SingleTwo {

	//1.创建私有构造方法
	private SingleTwo() {
		
	}
	
	//2.创建静态的该实例对象
	private static SingleTwo instance = null;
	
	//3.创建开放的静态方法提供实例对象
	public static SingleTwo getInstance() {
		if(instance==null)
			instance = new SingleTwo();
		return instance;
	}
}
