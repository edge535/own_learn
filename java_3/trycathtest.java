package test.jv3;

public class trycathtest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		trycathtest tct = new trycathtest();
//		int result = tct.test();
//		System.out.println("test()����ִ����ϣ�����ֵΪ��"+result);
//		int result2 = tct.test2();
//		System.out.println("test2()����ִ�����");
		int result3 = tct.test3();
		System.out.println("test3()����ִ�����,����ֵΪ��"+result3);
	}
	
	
	/*
	 * divider(������
	 * result�������
	 * ÿ��ѭ��divider-1 �� result=result+100/divider
	 * */
	public int test() {
		int divider = 10;
		int result = 100;
		try {
			while(divider > -1) {
				divider--;
				result = result + 100/divider;
			}
			return result;
		}catch(Exception e){
			e.printStackTrace();
			System.out.println("ѭ���׳��쳣��");
			return -1;
		}
	}
	
	public int test2() {
		int divider = 10;
		int result = 100;
		try {
			while(divider > -1) {
				divider--;
				result = result + 100/divider;
			}
			return result;
		}catch(Exception e){
			e.printStackTrace();
			System.out.println("ѭ���׳��쳣��");
			return result = 999;
		}finally {
			System.out.println("������finally");
			System.out.println("������result���ҵ�ֵ�ǣ�"+result);
		}
	}
	
	public int test3() {
		int divider = 10;
		int result = 100;
		try {
			while(divider > -1) {
				divider--;
				result = result + 100/divider;
			}
		}catch(Exception e){
			e.printStackTrace();
			System.out.println("ѭ���׳��쳣��");
		}finally {
			System.out.println("������finally");
			System.out.println("������result���ҵ�ֵ�ǣ�"+result);
		}
		System.out.println("������test3()");
		return 1111;
	}
	
	
	
}
