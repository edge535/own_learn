package test.jv2;

public class smartphone extends Telphone implements Iplaygame {

	@Override
	public void call() {
		// TODO Auto-generated method stub
		System.out.println("ͨ����������绰");
	}

	@Override
	public void send() {
		// TODO Auto-generated method stub
		System.out.println("ͨ��������������");
	}

	public void playgame() {
		System.out.println("����������Ϸ�Ĺ���");
	}
}
