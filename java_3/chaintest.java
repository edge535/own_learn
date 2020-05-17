package test.jv3;

public class chaintest {
	/*
	 * test1() 抛出 喝大了 异常
	 * test2（） 调用test1（） 捕获 喝大了 异常， 并且包装成运行时异常，积雪抛出
	 * main中 调用test2 捕获test2（）方法抛出的异常
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
		throw new drunkexception("喝酒别开车");
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
