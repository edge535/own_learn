package test.jv2;
import java.util.Scanner;

public class RentCarInit {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		RentCarInit I = new RentCarInit();
		Scanner input = new Scanner(System.in);
		System.out.println("欢迎使用租车系统：");
		System.out.println("您是否要租车：1是，0否");
		if(input.nextInt()==1)
			I.rentSys();
		else
			System.out.println("再见");
	}
	
	
	public void rentSys() {
		System.out.println("您可租车的类型及价目表：");
		System.out.println("序号           汽车名称          租     金                 容      量");
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
					System.out.format("%-1s%16s元/天     载货%1d吨", ele[0], ele[1], trans);
				break;
			default:
				if(trans == 0)
					System.out.format("%-1s%7s元/天    载客%1d位", ele[0], ele[1], seat);
				else
					System.out.format("%-1s%7s元/天    载客%1d位    载货%1s吨", ele[0], ele[1], seat, trans);
		}
			System.out.println("");
			j++;
		}
		System.out.println("请输入您要租车的数量");
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
			System.out.println("请输入第"+re_count+"辆车的序号:");
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
		System.out.println("请输入租车的天数:");
		count_cost *= input2.nextInt();
		System.out.println("您的账单:");
		System.out.println("可以坐人的车有:");
		System.out.print("          "+r);
		System.out.println("坐位共计:"+count_seat+"位");
		System.out.println("可以载货的车有:");
		System.out.print("          "+h);
		System.out.println("载货共计:"+count_trans+"吨");
		System.out.println(" 总价格:"+count_cost);
		
		
		
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
