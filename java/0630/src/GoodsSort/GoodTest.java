package GoodsSort;
import java.util.*;
public class GoodTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Goods g1 = new Goods("s0001","手机",2000);
		Goods g2 = new Goods("s0002","冰箱",5000);
		Goods g3 = new Goods("s0003","电视机",3000);
		List<Goods> list = new ArrayList<Goods>();
		list.add(g1);
		list.add(g2);
		list.add(g3);
		System.out.println("排序前:");
		for(Goods g:list) {
			System.out.println(g);
		}
		Collections.sort(list);
		System.out.println("排序后:");
		for(Goods g:list) {
			System.out.println(g);
		}
	}

}
