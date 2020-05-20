package test.jv4;
import java.util.*;
public class collectiontest {
	
	/**
	 * ��integer���͵�list��������
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
			System.out.println("�ɹ����������"+k);
		}
		System.out.println("----------����ǰ------------");
		for(Integer integer : integerList) {
			System.out.println("Ԫ�أ�"+integer);
		}
		Collections.sort(integerList);
		System.out.println("----------�����------------");
		for(Integer integer : integerList) {
			System.out.println("Ԫ�أ�"+integer);
		}
	}
	
	/**
	 * ��string���͵�list��������
	 */
	public void testSort2() {
		List<String> stringlist = new ArrayList<String>();
		stringlist.add("microsoft");
		stringlist.add("google");
		stringlist.add("lenovo");
		System.out.println("----------����ǰ------------");
		for(String string : stringlist) {
			System.out.println("Ԫ�أ�"+string);
		}
		Collections.sort(stringlist);
		System.out.println("----------�����------------");
		for(String string : stringlist) {
			System.out.println("Ԫ�أ�"+string);
		}
	}
	
	
	public void testSort3() {
		List<student> studentlist = new ArrayList<student>();
		Random random = new Random();
		studentlist.add(new student(random.nextInt(1000)+"","cand"));
		studentlist.add(new student(random.nextInt(1000)+"","bob"));
		studentlist.add(new student(random.nextInt(1000)+"","anna"));
		studentlist.add(new student(10000+"","beyang"));
		System.out.println("----------����ǰ------------");
		for(student student:studentlist) {
			System.out.println("ѧ����"+student.id+","+student.name);
		}
		Collections.sort(studentlist);
		System.out.println("----------�����------------");
		for(student student:studentlist) {
			System.out.println("ѧ����"+student.id+","+student.name);
		}
		System.out.println("----------�������������------------");
		Collections.sort(studentlist, new studentComparator());
		for(student student:studentlist) {
			System.out.println("ѧ����"+student.id+","+student.name);
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
