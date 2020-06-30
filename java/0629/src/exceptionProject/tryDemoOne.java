package exceptionProject;

import java.util.InputMismatchException;
import java.util.Scanner;

public class tryDemoOne {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int one = 12;
		int two = 2;
		System.out.println("one和two的商是："+(one/two));
		
		Scanner input = new Scanner(System.in);
//		System.out.println("=====运算开始=====");
//		try {
//			System.out.print("请输入第一个整数>");
//			one = input.nextInt();
//			System.out.print("请输入第二个整数>");
//			two = input.nextInt();
//			System.out.println("one和two的商是："+(one/two));
//		}catch(ArithmeticException e){
//			System.out.println("程序出错：除数不能为零");
//			System.out.println(e);
//		}catch(InputMismatchException e){
//			System.out.println("程序出错：只能输入整数");
//			System.out.println(e);
//		}catch(Exception e){
//			System.out.println("出现了错误");
//		}finally {
//			System.out.println("finally中的语句一定被执行");
//		}
//		System.out.println("=====运算结束=====");
//	}
		
		try {
			int result = test();
			System.out.println("one和two的商是："+result);
		} catch (ArithmeticException e) {
			System.out.println("除数不能为零");
		}catch(InputMismatchException e) {
			System.out.println("只能输入整数");
		}
	
	}
	
	
	public static int test() throws ArithmeticException, InputMismatchException{
		Scanner input = new Scanner(System.in);
		System.out.println("=====运算开始=====");

		System.out.print("请输入第一个整数>");
		int one = input.nextInt();
		System.out.print("请输入第二个整数>");
		int two = input.nextInt();
		System.out.println("=====运算结束=====");
		return one / two;
	}
}
