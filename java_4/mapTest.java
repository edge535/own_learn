package test.jv4;
import java.util.*;
import java.util.Map.Entry;

public class mapTest {

	/**
	 * ������װѧ�����͵Ķ���
	 * @param args
	 */
	public Map<String, student> students;
	
	public mapTest(){
		this.students = new HashMap<String, student>();
	}
	
	/**
	 * ������ӣ�����ѧ��ID�� �ж��Ƿ�ռ��
	 * ��δ��ռ�ã������������������µ�ѧ�����󣬲�����ӵ�student��
	 * @param args
	 */
	public void testPut() {
		Scanner console = new Scanner(System.in);
		int i =0;
		while(i<3) {
			System.out.println("������ѧ��ID:");
			String ID = console.next();
			//�ж�ID�Ƿ�ռ��
			student st = students.get(ID);
			if(st == null) {
				//��ʾ����ѧ������
				System.out.println("����ѧ��������");
				String name = console.next();
				//����ѧ������
				student newstudnet = new student(ID, name);
				students.put(ID, newstudnet);
				System.out.println("�ɹ����ѧ��"+newstudnet.name);
				i++;
			}else {
				System.out.println("ѧ�� ID�Ѿ���ռ��");
				continue;
			}
		}
	}
	
	/**
	 * ����map��keyset����
	 * @param args
	 */
	public void testkeyset() {
		System.out.println("�ܹ���:"+students.size()+"��ѧ��");
		// ͨ��keyset����������map�����е�set����
		Set<String> keyset = students.keySet();
		for(String stuID : keyset) {
			student st = students.get(stuID);
			if(st != null) {
				System.out.println("ѧ��:"+st.name);
			}
		}
	}
	
	/**
	 * ɾ��map�����е�ӳ��
	 * @param args
	 */
	public void testremove() {
		Scanner console = new Scanner(System.in);
		while(true) {
			System.out.println("������Ҫɾ����ѧ��ID:");
			//��ȡ�Ӽ��������ID
			
			String ID = console.next();
			//�жϸ�ID�Ƿ��ж�Ӧ��ѧ������
			student st = students.get(ID);
			if(st == null) {
				System.out.println("��ID������");
				continue;
			}else {
				students.remove(ID);
				System.out.println("�ɹ�ɾ��ѧ��"+st.name);
				break;
			}
		}
	}
	
	/**
	 * ͨ��entryset��������map
	 * @param args
	 */
	public void testentryset() {
		Set<Entry<String, student>> entryset = students.entrySet();
		for(Entry<String, student> entry:entryset) {
			System.out.println("ȡ�ü���"+entry.getKey());
			System.out.println("ȡ��ֵ��"+entry.getValue().name);
		}
	}
	
	/**
	 * ʹ��put�����޸�map�е�����ӳ��
	 * @param args
	 */
	public void testmodify() {
		System.out.println("������Ҫ�޸ĵ�ѧ��ID��");
		Scanner console = new Scanner(System.in);
		while(true) {
			String stuID = console.next();
			student student = students.get(stuID);
			if(student == null) {
				System.out.println("��ID�����ڣ�����������");
				continue;
			}else {
				System.out.println("��ǰIDѧ��Ϊ��"+student.name);
				System.out.println("�������µ�ѧ��������");
				String name = console.next();
				student ns = new student(stuID, name);
				students.put(stuID, ns);
				System.out.println("�޸����");
				break;
			}
		}
	}
	
	/**
	 * ����map�У��Ƿ񺺰���ĳ��keyֵ����valueֵ
	 * @param args
	 */
	public void testontainskeyorvalue() {
		// ��ʾ����ѧ��ID
		System.out.println("������Ҫ��ѯ��ѧ��ID");
		Scanner console = new Scanner(System.in);
		String id = console.next();
		System.out.println("�������ѧ��IDΪ��"+id+",��ӳ������Ƿ���ڣ�"+students.containsKey((id)));
		if(students.containsKey(id))
			System.out.println("��Ӧ��ѧ��Ϊ:"+students.get(id).name);
		// ��ʾ����ѧ������
		System.out.println("������Ҫ��ѯ��ѧ������");
		String name = console.next();
		if(students.containsValue(new student(null, name)))
			System.out.println("��ѧ��ӳ����У��Ǵ��ڵ�");
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
