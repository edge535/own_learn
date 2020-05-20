package test.jv4;
import java.util.*;
public class collectiontest {
	
	/**
	 * 对integer类型的list进行排序
	 */
	public void testSort1() {
		List<Integer> integerList = new ArrayList<Integer>();
		Random random = new Random();
		Integer k;
		for(int i=0; i<10; i++) {
			do {
				k = random.nextInt(100);
			}while(integerList.contains(k));
			integerList.add(k);
			System.out.println("成功添加整数："+k);
		}
		System.out.println("----------排序前------------");
		for(Integer integer : integerList) {
			System.out.println("元素："+integer);
		}
		Collections.sort(integerList);
		System.out.println("----------排序后------------");
		for(Integer integer : integerList) {
			System.out.println("元素："+integer);
		}
	}
	
	/**
	 * 对string类型的list进行排序
	 */
	public void testSort2() {
		List<String> stringlist = new ArrayList<String>();
		stringlist.add("microsoft");
		stringlist.add("google");
		stringlist.add("lenovo");
		System.out.println("----------排序前------------");
		for(String string : stringlist) {
			System.out.println("元素："+string);
		}
		Collections.sort(stringlist);
		System.out.println("----------排序后------------");
		for(String string : stringlist) {
			System.out.println("元素："+string);
		}
	}
	
	
	public void testSort3() {
		List<student> studentlist = new ArrayList<student>();
		Random random = new Random();
		studentlist.add(new student(random.nextInt(1000)+"","cand"));
		studentlist.add(new student(random.nextInt(1000)+"","bob"));
		studentlist.add(new student(random.nextInt(1000)+"","anna"));
		studentlist.add(new student(10000+"","beyang"));
		System.out.println("----------排序前------------");
		for(student student:studentlist) {
			System.out.println("学生："+student.id+","+student.name);
		}
		Collections.sort(studentlist);
		System.out.println("----------排序后------------");
		for(student student:studentlist) {
			System.out.println("学生："+student.id+","+student.name);
		}
		System.out.println("----------按照姓名排序后------------");
		Collections.sort(studentlist, new studentComparator());
		for(student student:studentlist) {
			System.out.println("学生："+student.id+","+student.name);
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		collectiontest ct = new collectiontest();
		ct.testSort1();
		ct.testSort2();
		ct.testSort3();
	}

}
