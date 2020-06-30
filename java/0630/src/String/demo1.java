package String;

public class demo1 {
	public static void main(String[] args) {
		String str = "Java 编程 基础";  
		System.out.println(str.charAt(6));
		System.out.println(str.substring(5));
		System.out.println(str.substring(5,7));
		System.out.println("======================");
		System.out.println(str.indexOf('a'));
		System.out.println(str.lastIndexOf('a'));
		System.out.println(str.indexOf("编程"));
		System.out.println(str.indexOf('A'));
		
	}
	
}
