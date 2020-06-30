package set_array_key;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class StringSort {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<String> list = new ArrayList<String>();
		list.add("orange");
		list.add("blue");
		list.add("yellow");
		list.add("gray");
		
		System.out.println("排序前:");
		for(String n : list) {
			System.out.print(n+" ");
		}
		Collections.sort(list);
		System.out.println();
		System.out.println("排序后:");
		for(String n : list) {
			System.out.print(n+" ");
		}
	}

}
