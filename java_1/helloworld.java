package test.jv;
import java.util.Scanner;
/*
 * ʹ��scanner�������ȡ�û������ֵ
 * scanner��λ��java.util����
 * ���裺
 * 	1.����jav.util.scanner
 * 	2.����scanner����
 * 	3.���ܲ������û������ֵ
*/
public class helloworld {
	public static void main(String[] args) {
		System.out.print("�����뿼�Գɼ�:"); //+An�����ỻ��
		Scanner input = new Scanner(System.in); //����Scanner����
		int score = input.nextInt(); // ��ȡ�û�����ĳɼ��������ڱ�����
		int count = 0;
		System.out.println("�ӷ�ǰ�ĳɼ���"+score);
		while(score<60) {
			score++;
			count++;
		}
		System.out.println("�ӷֺ�ĳɼ���"+score);
		System.out.println("�ӷֵĴ�����"+count);
	}
}