package test.jv4;
import java.util.*;

public class setTest {
	public List<course> coursesToSelect;
	private Scanner console;
	public student student;
	
	public setTest() {
		coursesToSelect = new ArrayList<course>();
		console = new Scanner(System.in);
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
	
	/**
	 * 测试list的contains方法
	 * @param args
	 */
	public void testlistcontains() {
		course course = coursesToSelect.get(0);
		System.out.println("取得课程"+course.name);
		System.out.println("备选课程中是否包含课程："+course.name+","+coursesToSelect.contains(course));
		//提示输入课程名称
		System.out.println("请输入课程名称：");
		String name = console.next();
		//创建一个新的课程对象，ID和名称，与course对象一样
		course course2 = new course();
		course2.name = name;
		System.out.println("新创建课程"+course2.name);
		System.out.println("备选课程中是否包含课程："+course2.name+","+coursesToSelect.contains(course2));
		if(coursesToSelect.contains(course2)) {
			System.out.println("课程"+course2.name+"的索引位置为："+coursesToSelect.indexOf(course2));
		}
	}
	
	public void createStudentAndSelectCourse() {
		//创建一个学生对象
		student = new student("1", "小明");
		System.out.println("欢迎学生"+student.name+"选课！");
		Scanner console = new Scanner(System.in);
		
		for(int i=0; i<3; i++) {
			System.out.println("请输入课程ID：");
			String courseId = console.next();
			for(course cr:coursesToSelect) {
				if(cr.id.equals(courseId)) {
					student.sourses.add(cr);
				}
			}
		}
		//打印输出，学生所学的课程;
		testForEachSet(student);
	}
	
	
	/**
	 * 测试set的contains方法
	 * @param args
	 */
	public void testsetcontains() {
		//提示输入课程名称
		System.out.println("请输入学生已的课程名称");
		String name = console.next();
		course course2 = new course();
		course2.name = name;
		System.out.println("新创建课程"+course2.name);
		System.out.println("备选课程中是否包含课程："+course2.name+","+student.sourses.contains(course2));
	}
	
	
	public static void main(String[] args) {
		setTest st = new setTest();
		st.testAdd();
		st.testlistcontains();
//		st.testforeach();
//		st.createStudentAndSelectCourse();
//		st.testsetcontains();
//		
	}
	
	
	public void testForEachSet(student student) {
		for(course cr : student.sourses) {
			System.out.println("选择了课程："+cr.id+":"+cr.name);
		}
	}
}
