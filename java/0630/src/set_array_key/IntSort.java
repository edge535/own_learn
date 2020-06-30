package set_array_key;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class IntSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//对存储在list中的的整形数据进行排序
		List<Integer> list = new ArrayList<Integer>();
		list.add(5);
		list.add(9);
		list.add(2);
		list.add(1);
		System.out.println("排序前：");
		for(int n : list) {
			System.out.print(n + " ");
		}
		Collections.sort(list);
		System.out.println();
		System.out.println("排序后：");
		for(int n : list) {
			System.out.print(n + " ");
		}
		
	}

}
