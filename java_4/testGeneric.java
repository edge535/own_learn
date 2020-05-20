package test.jv4;
import java.util.*;

public class testGeneric {
	// 范型
	public List<course> courses;
	
	public testGeneric() {
		this.courses = new ArrayList<course>();
	}
	
	/**
	 * 测试添加
	 */
	public void testAdd() {
		course cr1 = new course("1", "大学语文");
		courses.add(cr1);
		//courses.add("添加一条奇怪的东西");
		course cr2 = new course("2", "java基础");
		courses.add(cr2);
	}
	
	/**
	 * 虚幻遍历
	 */
	public void foreach() {
		for(course cr : courses) {
			System.out.println(cr.id+cr.name);
		}
	}
	
	/**
	 * 可以添加子类型的对象实例
	 * @param args
	 */
	public void testchid() {
		childrenCourse ccr = new childrenCourse();
		ccr.id = "3";
		ccr.name = "我是子类型的实力";
		courses.add(ccr);
		foreach();
	}
	
	/**
	 * 范形不能使用基本类型，需要使用包装类
	 * @param args
	 */
	public void testBaic() {
		List<Integer> list = new ArrayList<Integer>();
		list.add(1);
		System.out.println("基本类型的包装类"+list.get(0));
		
	}
	
	public static void main(String[] args) {
		testGeneric tg = new testGeneric();
		tg.testAdd();
		tg.foreach();
		tg.testchid();
		tg.testBaic();
	}
}
