package test.jv2;

public class init_telphone {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Telphone tel1 = new cellphone();
		tel1.call();
		tel1.send();
		Telphone tel2 = new smartphone();
		tel2.call();
		tel2.send();
		
		Iplaygame ip1 = new smartphone();
		Iplaygame ip2 = new psp();
		ip1.playgame();
		ip2.playgame();
		
		Iplaygame ip3 = new Iplaygame() {
			
			@Override
			public void playgame() {
				// TODO Auto-generated method stub
				System.out.println("使用匿名内部类的方式实现接口");
			}
		};
		ip3.playgame();
		
		new Iplaygame() {
			
			@Override
			public void playgame() {
				// TODO Auto-generated method stub
				System.out.println("使用匿名内部类的方式实现接口2");
			}
		}.playgame();
		
		
		
		
	}
}
