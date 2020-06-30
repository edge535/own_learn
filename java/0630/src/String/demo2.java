package String;

import java.io.UnsupportedEncodingException;

public class demo2 {

	public static void main(String[] args) throws UnsupportedEncodingException {
		// TODO Auto-generated method stub
		//字符串和byte数组之间的相互转换
		String str = new String("JAVA 编程 基础");
		byte[] arrs = str.getBytes();
		for(int i=0; i<arrs.length; i++) {
			System.out.print(arrs[i]+" ");
		}
		
		System.out.println();
		String str1 = new String(arrs,"GBK");
		System.out.println(str1);
	}

}
