package exceptionProject;

import java.util.Scanner;

public class tryDemotwo {

	public static void main(String[] args) {
		testAge();
	}
	
	public static void testAge() {
		try {
			System.out.println("请输入年龄>");
			Scanner input = new Scanner(System.in);
			int age = input.nextInt();
			if(age<18||age>80) {
				//throw new Exception("18岁以下，80岁以上需要亲属陪同");
				throw new hotelAgeException();
			}else {
				System.out.println("欢迎入住");
			}
		}catch (Exception e) {
				// TODO Auto-generated catch block
				System.out.println(e.getMessage());
		}
	}
}
