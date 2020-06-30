package set_array_key;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class CatTest {

	public static void main(String[] args) {
		Cat huahua = new Cat("花花",12,"英国短毛猫");
		Cat fanfan = new Cat("凡凡",3,"中华田园猫猫");
		Set<Cat> haset = new HashSet<Cat>();
		haset.add(huahua);
		haset.add(fanfan);
		Iterator<Cat> it = haset.iterator();
		while(it.hasNext()) {
			System.out.println(it.next());
		}
		
		//添加一个和花花一样的猫
		Cat huahua01 = new Cat("花花",12,"英国短毛猫");
		System.out.println("***********************");
		System.out.println("添加重复数据后的set");
		haset.add(huahua01);
		it = haset.iterator();
		while(it.hasNext()) {
			System.out.println(it.next());
		}
		
		//重新插入一个新宠物猫
		System.out.println("***********************");
		Cat huahua02 = new Cat("花花二代",2,"英国短毛猫");
		haset.add(huahua02);
		//在集合中查找
		it = haset.iterator();
		while(it.hasNext()) {
			Cat c = (Cat)it.next();
			if(c.getName().equals("花花")) {
				System.out.println("花花找到了！");
				System.out.println(c);
				break;
			}else {
				System.out.println("花花没找到");
			}
		}
		
		//删除花花二代 并重新输出
		System.out.println("***********************");
		for(Cat cat:haset) {
			if("花花二代".equals(cat.getName())) {
				haset.remove(cat);
			}
		}
		for(Cat cat:haset) {
			System.out.println(cat);
		}
		
		//清空
		System.out.println("***********************");
		//haset.clear();
		haset.removeAll(haset);
		System.out.println(haset.size());
		
	}
	
}
