package test.jv2;
import java.util.Scanner;

public class RentCarInit {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		RentCarInit I = new RentCarInit();
		Scanner input = new Scanner(System.in);
		System.out.println("��ӭʹ���⳵ϵͳ��");
		System.out.println("���Ƿ�Ҫ�⳵��1�ǣ�0��");
		if(input.nextInt()==1)
			I.rentSys();
		else
			System.out.println("�ټ�");
	}
	
	
	public void rentSys() {
		System.out.println("�����⳵�����ͼ���Ŀ��");
		System.out.println("���           ��������          ��     ��                 ��      ��");
		RentCar[] car = initCar();
		int j=1;
		for(RentCar c : car) {
			String[] ele = c.getElement();
			System.out.print(j+".    ");
			int seat = Integer.valueOf(ele[2]);
			int trans = Integer.valueOf(ele[3]);
			switch(seat) {
			case 0:
				if(trans!=0)
					System.out.format("%-1s%16sԪ/��     �ػ�%1d��", ele[0], ele[1], trans);
				break;
			default:
				if(trans == 0)
					System.out.format("%-1s%7sԪ/��    �ؿ�%1dλ", ele[0], ele[1], seat);
				else
					System.out.format("%-1s%7sԪ/��    �ؿ�%1dλ    �ػ�%1s��", ele[0], ele[1], seat, trans);
		}
			System.out.println("");
			j++;
		}
		System.out.println("��������Ҫ�⳵������");
		Scanner input2 = new Scanner(System.in);
		int count = input2.nextInt();
		int re_count = 0;
		int count_cost = 0;
		int count_seat = 0;
		int count_trans = 0;
		String r = "";
		String h = "";
		while(re_count != count) {
			re_count++;
			System.out.println("�������"+re_count+"���������:");
			String[] ele = car[input2.nextInt()-1].getElement();
			//RentCarInit I = new RentCarInit();
			if(Integer.valueOf(ele[2]) == 0) {
				h += (ele[0]+" ");
			}else if(Integer.valueOf(ele[2]) != 0 && Integer.valueOf(ele[3]) != 0) {
				r += (ele[0]+" ");
				h += (ele[0]+" ");
			}else {
				r += (ele[0]+" ");
			}
			count_cost += Integer.valueOf(ele[1]);
			count_seat += Integer.valueOf(ele[2]);
			count_trans += Integer.valueOf(ele[3]);	
		}
		System.out.println("�������⳵������:");
		count_cost *= input2.nextInt();
		System.out.println("�����˵�:");
		System.out.println("�������˵ĳ���:");
		System.out.print("          "+r);
		System.out.println("��λ����:"+count_seat+"λ");
		System.out.println("�����ػ��ĳ���:");
		System.out.print("          "+h);
		System.out.println("�ػ�����:"+count_trans+"��");
		System.out.println(" �ܼ۸�:"+count_cost);
		
		
		
	}
	


	public RentCar[] initCar() {
		RentCar[] car = {
				new BeRentCar(1, 500, 4, 0),
				new BeRentCar(2, 400, 4, 0),
				new BeRentCar(3, 450, 4, 2),
				new BeRentCar(4, 800, 20, 0),
				new BeRentCar(5, 400, 0, 4),
				new BeRentCar(6, 1000, 0, 20)
		};
		return car;
	}
	
	
	
}
