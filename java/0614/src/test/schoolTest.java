package test;
import model.Student;
import model.Subject;

public class schoolTest {

	public static void main(String[] args) {
		//测试subject
		Subject sub1 = new Subject("计算机科学与应用","J0001",4);
//		System.out.println(sub1.info());
//		System.out.println("====================");
		Student stu1 = new Student("S01","张三","男",18);
//		System.out.println(stu1.info());
//		Student stu2 = new Student("S02","李四","女",17);
//		System.out.println(stu2.introduction("计算机科学与应用",4));
//		Student stu3 = new Student("S03","王五","男",18);
//		System.out.println(stu3.introduction(sub1));
//		
//		Student stu4 = new Student("S04","张四","男",18,sub1);
//		System.out.println(stu4.introduction());
		
		
//		System.out.println("=================================");
		sub1.addStudent(stu1);
//		sub1.addStudent(stu2);
//		sub1.addStudent(stu3);
		System.out.println(sub1.getSubjuectName()+"的专业中已有"+sub1.getStudentNum()+"名学生报名");
	}

}
