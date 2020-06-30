package set_array_key;

import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;

public class goodTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner console = new Scanner(System.in);
		Map<String,Good> goodMap = new HashMap<String,Good>();
		int i=0;
		while(i<3) {
			System.out.println("请输入第"+(i+1)+"条商品的信息:");
			System.out.println("请输入商品编号：");
			String goodID = console.next();
			if(goodMap.containsKey(goodID)) {
				System.out.println("该商品编号已经存在，请重新输入！");
				continue;
			}
			System.out.println("请输入商品名字：");
			String goodName = console.next();
			System.out.println("请输入商品价格：");
			double goodPrice;
			try {
				goodPrice = console.nextDouble();
			}catch(InputMismatchException e){
				System.out.println("商品价格的格式不正确");
				console.next();
				continue;
			}
			Good good = new Good(goodID,goodName,goodPrice);
			goodMap.put(goodID, good);
			i++;
		}
		//遍历Map，输出商品信息
		System.out.println("商品的全部信息为：");
		Iterator<Good> itGood = goodMap.values().iterator();
		while(itGood.hasNext()) {
			System.out.println(itGood.next());
		}
		
		
		
	}

}
