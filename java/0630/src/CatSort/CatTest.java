package CatSort;

import java.util.*;

public class CatTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//按名字升序排序
		Cat huahua = new Cat("huahua",5,"布偶猫");
		Cat fanfan = new Cat("fanfan",2,"金渐层");
		Cat maomao = new Cat("maomao",9,"中华田园猫");
		List<Cat> list = new ArrayList<Cat>();
		list.add(huahua);
		list.add(fanfan);
		list.add(maomao);
		
		System.out.println("排序前：");
		for(Cat c : list) {
			System.out.println(c);
		}
		//进行排序
		Collections.sort(list, new NameComparator());
		
		System.out.println("名字升序排序后：");
		for(Cat c : list) {
			System.out.println(c);
		}
		
		
		//按年龄进行降序
		Collections.sort(list, new AgeComparator());
		System.out.println("按年龄进行降序后：");
		for(Cat c : list) {
			System.out.println(c);
		}
	}

}
