package test.jv2;

public class dog extends animal {
	public void eat() {
		System.out.println("age:"+age+" name:"+name+" 狗具有吃东西的能力");
	}
	public dog() {
		System.out.println("dog 执行了");
	}
	@Override
	public String toString() {
		return "dog [age=" + age + ", name=" + name + "]";
	}
}
