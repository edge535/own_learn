package test.jv4;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

/*
 * 用于存放备选课程的list
 * */
public class listtest {
	/*
	 * 用于存放备选课程的list
	 * */
	public List coursesToSelect;
	public listtest(){
		this.coursesToSelect = new ArrayList();
	}
	
	
	/**
	 * 用于往coursesToSelect中添加备选课程
	 */
	public void testAdd() {
		course cr1 = new course("1","数据就结构");
		coursesToSelect.add(cr1); // 直接插入
		course temp = (course)coursesToSelect.get(0);
		System.out.println("添加了课程："+temp.id+":"+temp.name);
		
		course cr2 = new course("2", "C语言");
		coursesToSelect.add(0, cr2); // 在指定位置插入
		course temp2 = (course)coursesToSelect.get(0);
		System.out.println("添加了课程："+temp2.id+":"+temp2.name);
		
		//一下方法会抛出数组下标越界异常
//		course cr3 = new course("3","test");
//		coursesToSelect.add(4,cr3);
		
		course[] courses = {new course("3","离散数学"),new course("4","汇编语言")};
		coursesToSelect.addAll(Arrays.asList(courses)); // 插入多个
		course temp3 = (course)coursesToSelect.get(2);
		course temp4 = (course)coursesToSelect.get(3);
		System.out.println("添加了两门课程："+temp3.id+":"+temp3.name+";"+temp4.id+":"+temp4.name);
	
		course[] courses2 = {new course("5","高等数学"),new course("6","英语语言")};
		coursesToSelect.addAll(2, Arrays.asList(courses2)); //在指定位置插入多个
		course temp5 = (course)coursesToSelect.get(2);
		course temp6 = (course)coursesToSelect.get(3);
		System.out.println("添加了两门课程："+temp5.id+":"+temp5.name+";"+temp6.id+":"+temp6.name);
		
		coursesToSelect.add(cr1); // 直接插入
		course temp0 = (course)coursesToSelect.get(2);
		System.out.println("添加了课程："+temp0.id+":"+temp0.name);
	}
	
	/**
	 * 取得list中的元素
	 * @param args
	 */
	public void testget() {
		int size = coursesToSelect.size();
		System.out.println("有如下课程待选");
		for(int i=0; i<size;i++) {
			course cr = (course)coursesToSelect.get(i);
			System.out.println("课程"+cr.id+":"+cr.name);
		}
	}
	
	/***
	 * 通过迭代器遍历list
	 * @param args
	 */
	public void testiterator() {
		Iterator it = coursesToSelect.iterator();
		System.out.println("有如下课程待选 iterator");
		while(it.hasNext()) {
			course cr = (course)it.next();
			System.out.println("课程"+cr.id+":"+cr.name);
		}
	}
	
	/***
	 * 通过for each 方法访问
	 * @param args
	 */
	public void testforeach() {
		System.out.println("有如下课程待选for each");
		for(Object obj:coursesToSelect) {
			course cr = (course)obj;
			System.out.println("课程"+cr.id+":"+cr.name);
		}
	}
	
	/***
	 * 修改list中的元素
	 * @param args
	 */
	public void modify() {
		coursesToSelect.set(6, new course("7","马克思主义原理"));
		testforeach();
	}
	
	/***
	 * 删除list中元素
	 * @param args
	 */
	public void testremove() {
		course cr = (course)coursesToSelect.get(6);
		System.out.println("我是课程："+cr.id+":"+cr.name);
		coursesToSelect.remove(cr);
		testforeach();
	}
	
	public void testremoveall() {
		course[] cr = {(course)coursesToSelect.get(4),(course)coursesToSelect.get(5)};
		coursesToSelect.removeAll(Arrays.asList(cr));
		testforeach();
	}
	
	/***
	 * 往list中添加一些奇怪的东西
	 * @param args
	 */
	public void testtype() {
		coursesToSelect.add("我不是课程，我是字符串");
	}
	
	public static void main(String[] args) {
		listtest lt = new listtest();
		lt.testAdd();
		lt.testtype();
		lt.testforeach();
//		lt.testget();
//		lt.testiterator();
//		lt.testforeach();
//		lt.modify();
//		lt.testremove();
//		lt.testremoveall();
	}
}
