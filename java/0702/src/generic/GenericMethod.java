package generic;

public class GenericMethod {
	public <T> void printValue(T t) {
		System.out.println(t);
	}
	
	public <T> T getThis(T t){
		return t;
	}
	
	public static void main(String[] args) {
		GenericMethod gm = new GenericMethod();
		gm.printValue("hello");
		gm.printValue(123);
		gm.printValue(2.3f);
	}
}
