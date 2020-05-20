package test.jv4;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

/*
 * ���ڴ�ű�ѡ�γ̵�list
 * */
public class listtest {
	/*
	 * ���ڴ�ű�ѡ�γ̵�list
	 * */
	public List coursesToSelect;
	public listtest(){
		this.coursesToSelect = new ArrayList();
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
		
		coursesToSelect.add(cr1); // ֱ�Ӳ���
		course temp0 = (course)coursesToSelect.get(2);
		System.out.println("����˿γ̣�"+temp0.id+":"+temp0.name);
	}
	
	/**
	 * ȡ��list�е�Ԫ��
	 * @param args
	 */
	public void testget() {
		int size = coursesToSelect.size();
		System.out.println("�����¿γ̴�ѡ");
		for(int i=0; i<size;i++) {
			course cr = (course)coursesToSelect.get(i);
			System.out.println("�γ�"+cr.id+":"+cr.name);
		}
	}
	
	/***
	 * ͨ������������list
	 * @param args
	 */
	public void testiterator() {
		Iterator it = coursesToSelect.iterator();
		System.out.println("�����¿γ̴�ѡ iterator");
		while(it.hasNext()) {
			course cr = (course)it.next();
			System.out.println("�γ�"+cr.id+":"+cr.name);
		}
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
	
	/***
	 * �޸�list�е�Ԫ��
	 * @param args
	 */
	public void modify() {
		coursesToSelect.set(6, new course("7","���˼����ԭ��"));
		testforeach();
	}
	
	/***
	 * ɾ��list��Ԫ��
	 * @param args
	 */
	public void testremove() {
		course cr = (course)coursesToSelect.get(6);
		System.out.println("���ǿγ̣�"+cr.id+":"+cr.name);
		coursesToSelect.remove(cr);
		testforeach();
	}
	
	public void testremoveall() {
		course[] cr = {(course)coursesToSelect.get(4),(course)coursesToSelect.get(5)};
		coursesToSelect.removeAll(Arrays.asList(cr));
		testforeach();
	}
	
	/***
	 * ��list�����һЩ��ֵĶ���
	 * @param args
	 */
	public void testtype() {
		coursesToSelect.add("�Ҳ��ǿγ̣������ַ���");
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
