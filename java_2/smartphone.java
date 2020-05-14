package test.jv2;

public class smartphone extends Telphone implements Iplaygame {

	@Override
	public void call() {
		// TODO Auto-generated method stub
		System.out.println("通过语音来打电话");
	}

	@Override
	public void send() {
		// TODO Auto-generated method stub
		System.out.println("通过语音来发短信");
	}

	public void playgame() {
		System.out.println("具有了玩游戏的功能");
	}
}
