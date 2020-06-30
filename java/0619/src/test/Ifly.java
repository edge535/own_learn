package test;

public interface Ifly {
	default void fly() {
		System.out.println("来自接口的fly");
	};
	
	static void fly2() {
		System.out.println("来自接口的static");
	}
}
