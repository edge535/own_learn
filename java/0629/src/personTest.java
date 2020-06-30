
public class personTest {
	
	public static void main(String[] args) {
		person lili = new person();
		lili.age=12;
		
		/*
		//获取内部类 方法1：
		person.Heart myHeart = new person().new Heart();
		System.out.println(myHeart.beat());
		
		//获取内部类 方法2：
		myHeart = lili.new Heart();
		System.out.println(myHeart.beat());
		
		//获取内部类 方法3：
		myHeart = lili.getHeart();
		System.out.println(myHeart.beat());
		*/
		
		/*
		//静态内部类对象实例
		person.Heart myHeart = new person.Heart();
		System.out.println(myHeart.beat());
		
		person.Heart.say();
		*/
		
		System.out.println(lili.getHeart());
	}
	
}

