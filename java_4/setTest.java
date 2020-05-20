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
	 * ������coursesToSelect����ӱ�ѡ�γ�
	 */
	public void testAdd() {
		course cr1 = new course("1","���ݾͽṹ");
		coursesToSelect.add(cr1); // ֱ�Ӳ���
		course temp = (course)coursesToSelect.get(0);
		System.out.println("����˿γ̣�"+temp.id+":"+temp.name);
		
		course cr2 = new course("2", "C����");
		coursesToSelect.add(0, cr2); // ��ָ��λ�ò���
		course temp2 = (course)coursesToSelect.get(0);
		System.out.println("����˿γ̣�"+temp2.id+":"+temp2.name);
		
		//һ�·������׳������±�Խ���쳣
//		course cr3 = new course("3","test");
//		coursesToSelect.add(4,cr3);
		
		course[] courses = {new course("3","��ɢ��ѧ"),new course("4","�������")};
		coursesToSelect.addAll(Arrays.asList(courses)); // ������
		course temp3 = (course)coursesToSelect.get(2);
		course temp4 = (course)coursesToSelect.get(3);
		System.out.println("��������ſγ̣�"+temp3.id+":"+temp3.name+";"+temp4.id+":"+temp4.name);
	
		course[] courses2 = {new course("5","�ߵ���ѧ"),new course("6","Ӣ������")};
		coursesToSelect.addAll(2, Arrays.asList(courses2)); //��ָ��λ�ò�����
		course temp5 = (course)coursesToSelect.get(2);
		course temp6 = (course)coursesToSelect.get(3);
		System.out.println("��������ſγ̣�"+temp5.id+":"+temp5.name+";"+temp6.id+":"+temp6.name);
	}
	
	/***
	 * ͨ��for each ��������
	 * @param args
	 */
	public void testforeach() {
		System.out.println("�����¿γ̴�ѡfor each");
		for(Object obj:coursesToSelect) {
			course cr = (course)obj;
			System.out.println("�γ�"+cr.id+":"+cr.name);
		}
	}
	
	/**
	 * ����list��contains����
	 * @param args
	 */
	public void testlistcontains() {
		course course = coursesToSelect.get(0);
		System.out.println("ȡ�ÿγ�"+course.name);
		System.out.println("��ѡ�γ����Ƿ�����γ̣�"+course.name+","+coursesToSelect.contains(course));
		//��ʾ����γ�����
		System.out.println("������γ����ƣ�");
		String name = console.next();
		//����һ���µĿγ̶���ID�����ƣ���course����һ��
		course course2 = new course();
		course2.name = name;
		System.out.println("�´����γ�"+course2.name);
		System.out.println("��ѡ�γ����Ƿ�����γ̣�"+course2.name+","+coursesToSelect.contains(course2));
		if(coursesToSelect.contains(course2)) {
			System.out.println("�γ�"+course2.name+"������λ��Ϊ��"+coursesToSelect.indexOf(course2));
		}
	}
	
	public void createStudentAndSelectCourse() {
		//����һ��ѧ������
		student = new student("1", "С��");
		System.out.println("��ӭѧ��"+student.name+"ѡ�Σ�");
		Scanner console = new Scanner(System.in);
		
		for(int i=0; i<3; i++) {
			System.out.println("������γ�ID��");
			String courseId = console.next();
			for(course cr:coursesToSelect) {
				if(cr.id.equals(courseId)) {
					student.sourses.add(cr);
				}
			}
		}
		//��ӡ�����ѧ����ѧ�Ŀγ�;
		testForEachSet(student);
	}
	
	
	/**
	 * ����set��contains����
	 * @param args
	 */
	public void testsetcontains() {
		//��ʾ����γ�����
		System.out.println("������ѧ���ѵĿγ�����");
		String name = console.next();
		course course2 = new course();
		course2.name = name;
		System.out.println("�´����γ�"+course2.name);
		System.out.println("��ѡ�γ����Ƿ�����γ̣�"+course2.name+","+student.sourses.contains(course2));
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
			System.out.println("ѡ���˿γ̣�"+cr.id+":"+cr.name);
		}
	}
}
