package set_array_key;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class hashset {
	public static void main(String[] args) {
		Set hset = new HashSet();
		hset.add("blue");
		hset.add("red");
		hset.add("black");
		hset.add("yellow");
		hset.add("white");
		
		//显示集合中的内容
		System.out.println("集合中的元素为");
		Iterator it = hset.iterator();
		while(it.hasNext()) {
			System.out.print(it.next()+" ");
		}
		
		//在set中插入新元素
		hset.add("green");
		System.out.println();
		System.out.println("插入后集合中的元素为");
		it = hset.iterator();
		while(it.hasNext()) {
			System.out.print(it.next()+" ");
		}
		
		//插入重复元素
		hset.add("green");
		System.out.println();
		System.out.println("插入重复数据后集合中的元素为");
		it = hset.iterator();
		while(it.hasNext()) {
			System.out.print(it.next()+" ");
		}
		
	}
}
