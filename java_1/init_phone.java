package test.jv;

public class init_phone {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		Telphone phone = new Telphone();
//		phone.sendMessage();
//		phone.screen = 5.0f;
//		phone.cpu = 1.4f;
//		phone.mem = 2.0f;
//		phone.sendMessage();
//		phone.call();
//		Telphone phone = new Telphone(5.0f, 1.4f, 2.0f);
		Telphone phone2 = new Telphone();
		phone2.setScreen(16.5f);
		System.out.println(phone2.getScreen());
	}

}
