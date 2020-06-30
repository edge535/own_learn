
public class personTest2 {
	//根据传入的不同的人的类型，调用对应的read方法
	//方法1：
//	public void getRead(Man man) {
//		man.read();
//	}
//	public void getRead(Woman woman) {
//		woman.read();
//	}
	
	//方法2：
	public void getRead(person2 person) {
		person.read();
	}
	
	public static void main(String[] args) {
		personTest2 test = new personTest2();
//		
//		Man one = new Man();
//		Woman two = new Woman();
//		
//		test.getRead(one);
//		test.getRead(two);
		
		//方案3： 匿名内部类
		test.getRead(new person2() {

			@Override
			public void read() {
				// TODO Auto-generated method stub
				System.out.println("男生喜欢看科幻类书籍");
			}
			
		});
		
		test.getRead(new person2() {

			@Override
			public void read() {
				// TODO Auto-generated method stub
				System.out.println("女生喜欢读小说");
			}
			
		});
		
		
		
	}

}
