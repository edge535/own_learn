package test.jv3;

public class chaintest {
	/*
	 * test1() �׳� �ȴ��� �쳣
	 * test2���� ����test1���� ���� �ȴ��� �쳣�� ���Ұ�װ������ʱ�쳣����ѩ�׳�
	 * main�� ����test2 ����test2���������׳����쳣
	 * */
	public static void main(String[] args) {
		chaintest ct = new chaintest();
		try {
			ct.test2();
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}
	
	
	public void test1() throws drunkexception{
		throw new drunkexception("�ȾƱ𿪳�");
	}
	
	public void test2() {
		try {
			test1();
		} catch (drunkexception e) {
			// TODO: handle exception
			RuntimeException newexc = new RuntimeException(e);
			//newexc.initCause(e);
			throw newexc;
			
		}
	}
	
}
