package test.jv5;
import java.util.*;

public class test {
	List<String> StrList;
	
	public test() {
		StrList = new ArrayList<String>();
	}
	
	public void add() {
		Random r = new Random();
		StringBuilder sb = new StringBuilder();
		int str_count;
		int i;
		for(i=0; i<10; i++) {
			str_count = r.nextInt(9)+1;
			for(int j=0; j<str_count; j++) {
				int t = r.nextInt(94)+33;
				char c = (char)(t);
				sb.append(c);
			}
			if(!StrList.contains(sb)){
				StrList.add(sb.toString());
				sb.delete(0, sb.length());
			}else {
				i--;
			}
		}
	}
	
	public void show() {
		int j = 1;
		for(String i : StrList) {
			System.out.print("µÚ"+j+"¸ö: ");
			System.out.println(i);
			j++;
		}
	}
	
	
	
	
	public static void main(String[] args) {
		test t = new test();
		t.add();
		t.show();
	}
}