package test.jv2;

public class dog extends animal {
	public void eat() {
		System.out.println("age:"+age+" name:"+name+" �����гԶ���������");
	}
	public dog() {
		System.out.println("dog ִ����");
	}
	@Override
	public String toString() {
		return "dog [age=" + age + ", name=" + name + "]";
	}
}
