package test.jv;
import java.util.*;

public class demo2 {
	public static void main(String[] args) {
		int classNum = 3;
		int stuNum = 4;
		double sum = 0 ;
		double avg = 0;
		Scanner input = new Scanner(System.in);
		for(int i=1; i<=classNum; i++){
			System.out.println("***请输入第"+i+"个班级的成绩***");
			for(int j=1; j<=stuNum; j++) {
				System.out.println("请输入第"+j+"个学员的成绩");
				int score = input.nextInt();
				sum = sum + score;
			}
			avg = sum / stuNum;
			sum = 0;
			System.out.println("第"+i+"个班级学员的平均分为"+avg);
		}
	}
}
