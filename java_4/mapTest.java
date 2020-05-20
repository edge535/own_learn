package test.jv4;
import java.util.*;
import java.util.Map.Entry;

public class mapTest {

	/**
	 * 用来橙装学生类型的对象
	 * @param args
	 */
	public Map<String, student> students;
	
	public mapTest(){
		this.students = new HashMap<String, student>();
	}
	
	/**
	 * 测试添加，输入学生ID， 判断是否被占用
	 * 若未被占用，则输入姓名，创建新的学生对象，并且添加到student中
	 * @param args
	 */
	public void testPut() {
		Scanner console = new Scanner(System.in);
		int i =0;
		while(i<3) {
			System.out.println("请输入学生ID:");
			String ID = console.next();
			//判断ID是否被占用
			student st = students.get(ID);
			if(st == null) {
				//提示输入学生姓名
				System.out.println("输入学生姓名：");
				String name = console.next();
				//创建学生对象
				student newstudnet = new student(ID, name);
				students.put(ID, newstudnet);
				System.out.println("成功添加学生"+newstudnet.name);
				i++;
			}else {
				System.out.println("学生 ID已经被占用");
				continue;
			}
		}
	}
	
	/**
	 * 测试map的keyset方法
	 * @param args
	 */
	public void testkeyset() {
		System.out.println("总共有:"+students.size()+"名学生");
		// 通过keyset方法，返回map中所有的set集合
		Set<String> keyset = students.keySet();
		for(String stuID : keyset) {
			student st = students.get(stuID);
			if(st != null) {
				System.out.println("学生:"+st.name);
			}
		}
	}
	
	/**
	 * 删除map中已有的映射
	 * @param args
	 */
	public void testremove() {
		Scanner console = new Scanner(System.in);
		while(true) {
			System.out.println("请输入要删除的学生ID:");
			//获取从键盘输入的ID
			
			String ID = console.next();
			//判断该ID是否有对应的学生对象
			student st = students.get(ID);
			if(st == null) {
				System.out.println("该ID不存在");
				continue;
			}else {
				students.remove(ID);
				System.out.println("成功删除学生"+st.name);
				break;
			}
		}
	}
	
	/**
	 * 通过entryset方法遍历map
	 * @param args
	 */
	public void testentryset() {
		Set<Entry<String, student>> entryset = students.entrySet();
		for(Entry<String, student> entry:entryset) {
			System.out.println("取得键："+entry.getKey());
			System.out.println("取得值："+entry.getValue().name);
		}
	}
	
	/**
	 * 使用put方法修改map中的已有映射
	 * @param args
	 */
	public void testmodify() {
		System.out.println("请输入要修改的学生ID：");
		Scanner console = new Scanner(System.in);
		while(true) {
			String stuID = console.next();
			student student = students.get(stuID);
			if(student == null) {
				System.out.println("该ID不存在，请重新输入");
				continue;
			}else {
				System.out.println("当前ID学生为："+student.name);
				System.out.println("请输入新的学生姓名：");
				String name = console.next();
				student ns = new student(stuID, name);
				students.put(stuID, ns);
				System.out.println("修改完成");
				break;
			}
		}
	}
	
	/**
	 * 测试map中，是否汉包含某个key值或者value值
	 * @param args
	 */
	public void testontainskeyorvalue() {
		// 提示输入学生ID
		System.out.println("请输入要查询的学生ID");
		Scanner console = new Scanner(System.in);
		String id = console.next();
		System.out.println("您输入的学生ID为："+id+",在映射表中是否存在："+students.containsKey((id)));
		if(students.containsKey(id))
			System.out.println("对应的学生为:"+students.get(id).name);
		// 提示输入学生姓名
		System.out.println("请输入要查询的学生姓名");
		String name = console.next();
		if(students.containsValue(new student(null, name)))
			System.out.println("在学生映射表中，是存在的");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		mapTest mt = new mapTest();
		mt.testPut();
		mt.testkeyset();
//		mt.testremove();
//		mt.testentryset();
//		mt.testmodify();
//		mt.testentryset();
		mt.testontainskeyorvalue();
	}

	
}
