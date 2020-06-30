
public class person {
	int age;
	
	public Object getHeart() {
		//return new Heart();
		class  Heart{
			int age = 18;
			public String beat() {
				new person().eat();
				return new person().age+"心脏在跳动";
			}
			public void say() {
				System.out.println("hello");
			}
		}
		return new Heart().beat();
	}
		
	public void eat() {
		System.out.println("人会吃东西");
	}
	
/*
//成员内部类	
//	class Heart{
//		int age = 18;
//		public void eat() {
//			System.out.println("人会吃东西from Heart");
//		}
//		public String beat() {
//			person.this.eat();
//			return age+"心脏在跳动";
//		}
//	}
*/

/*
//静态内部类中，只能直接访问外部类的静态成员，要调用非静态，需要外部类的实例
//	public static class  Heart{
//		int age = 18;
//		public String beat() {
//			new person().eat();
//			return new person().age+"心脏在跳动";
//		}
//		public static void say() {
//			System.out.println("hello");
//		}
//	}
*/
	
	
}
