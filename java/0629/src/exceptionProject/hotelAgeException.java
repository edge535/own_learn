package exceptionProject;

public class hotelAgeException extends Exception {
	public hotelAgeException() {
		super("18岁以下，80岁以上需要亲属陪同");
	}
}
