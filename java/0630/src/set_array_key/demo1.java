package set_array_key;

import java.util.ArrayList;
import java.util.List;

public class demo1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList list = new ArrayList();
		list.add("java");
		list.add("C");
		list.add("C++");
		list.add("Go");
		list.add("swift");
		list.add(999);
		System.out.println("列表中元素的个数为："+list.size());
		System.out.println("=============================");
		for(int i=0; i<list.size(); i++) {
			System.out.print(list.get(i)+",");
		}
		//移除c++
		//list.remove(2);
		list.remove("C++");
		System.out.println("=============================");
		System.out.println("移除C++后：");
		for(int i=0; i<list.size(); i++) {
			System.out.print(list.get(i)+",");
		}
	}

}
