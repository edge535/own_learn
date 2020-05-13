package test.jv;
import java.util.Scanner;
/*
 * 使用scanner工具类获取用户输入的值
 * scanner类位于java.util包中
 * 步骤：
 * 	1.导入jav.util.scanner
 * 	2.创建scanner对象
 * 	3.接受并保存用户输入的值
*/
public class helloworld {
	public static void main(String[] args) {
		System.out.print("请输入考试成绩:"); //+An输出后会换行
		Scanner input = new Scanner(System.in); //创建Scanner对象
		int score = input.nextInt(); // 获取用户输入的成绩并保存在变量中
		int count = 0;
		System.out.println("加分前的成绩："+score);
		while(score<60) {
			score++;
			count++;
		}
		System.out.println("加分后的成绩："+score);
		System.out.println("加分的次数："+count);
	}
}