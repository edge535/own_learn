package test.jv3;

public class trycathtest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		trycathtest tct = new trycathtest();
//		int result = tct.test();
//		System.out.println("test()方法执行完毕，返回值为："+result);
//		int result2 = tct.test2();
//		System.out.println("test2()方法执行完毕");
		int result3 = tct.test3();
		System.out.println("test3()方法执行完毕,返回值为："+result3);
	}
	
	
	/*
	 * divider(除数）
	 * result（结果）
	 * 每次循环divider-1 ； result=result+100/divider
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
			System.out.println("循环抛出异常！");
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
			System.out.println("循环抛出异常！");
			return result = 999;
		}finally {
			System.out.println("这里是finally");
			System.out.println("这里是result，我的值是："+result);
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
			System.out.println("循环抛出异常！");
		}finally {
			System.out.println("这里是finally");
			System.out.println("这里是result，我的值是："+result);
		}
		System.out.println("这里是test3()");
		return 1111;
	}
	
	
	
}
