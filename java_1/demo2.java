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
			System.out.println("***�������"+i+"���༶�ĳɼ�***");
			for(int j=1; j<=stuNum; j++) {
				System.out.println("�������"+j+"��ѧԱ�ĳɼ�");
				int score = input.nextInt();
				sum = sum + score;
			}
			avg = sum / stuNum;
			sum = 0;
			System.out.println("��"+i+"���༶ѧԱ��ƽ����Ϊ"+avg);
		}
	}
}
