package String;

public class demo3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str1 = "imooc";
		String str2 = "imooc";
		String str3 = new String("imooc");
		System.out.println("str1 == str2 内容 : "+(str1.equals(str2)));
		System.out.println("str1 == str3 内容 : "+(str1.equals(str3)));
		System.out.println("str1 == str2 地址 : "+(str1==(str2)));
		System.out.println("str1 == str3 地址 : "+(str1==(str3)));
		
		String s3 = new String("hello,imooc");
		System.out.println(s3.substring(0,5));
	}

}
