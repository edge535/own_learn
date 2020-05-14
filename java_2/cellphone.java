package test.jv2;

public class cellphone extends Telphone {

	@Override
	public void call() {
		// TODO Auto-generated method stub
		System.out.println("通过键盘来打电话");
	}

	@Override
	public void send() {
		// TODO Auto-generated method stub
		System.out.println("通过键盘来打发短信");
	}

}
