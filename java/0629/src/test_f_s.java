
public class test_f_s {
	public static void main(String[] args) {
		test_f ff = new test_f();
		test_s sff = (test_s) ff;
		System.out.println(
				sff instanceof test_f
				);
		System.out.println(
				sff instanceof test_s
				);
		
	}
}
