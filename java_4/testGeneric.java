package test.jv4;
import java.util.*;

public class testGeneric {
	// ����
	public List<course> courses;
	
	public testGeneric() {
		this.courses = new ArrayList<course>();
	}
	
	/**
	 * �������
	 */
	public void testAdd() {
		course cr1 = new course("1", "��ѧ����");
		courses.add(cr1);
		//courses.add("���һ����ֵĶ���");
		course cr2 = new course("2", "java����");
		courses.add(cr2);
	}
	
	/**
	 * ��ñ���
	 */
	public void foreach() {
		for(course cr : courses) {
			System.out.println(cr.id+cr.name);
		}
	}
	
	/**
	 * ������������͵Ķ���ʵ��
	 * @param args
	 */
	public void testchid() {
		childrenCourse ccr = new childrenCourse();
		ccr.id = "3";
		ccr.name = "���������͵�ʵ��";
		courses.add(ccr);
		foreach();
	}
	
	/**
	 * ���β���ʹ�û������ͣ���Ҫʹ�ð�װ��
	 * @param args
	 */
	public void testBaic() {
		List<Integer> list = new ArrayList<Integer>();
		list.add(1);
		System.out.println("�������͵İ�װ��"+list.get(0));
		
	}
	
	public static void main(String[] args) {
		testGeneric tg = new testGeneric();
		tg.testAdd();
		tg.foreach();
		tg.testchid();
		tg.testBaic();
	}
}
