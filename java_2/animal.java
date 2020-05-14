package test.jv2;

public class animal {
	public int age = 10;
	public String name;
	public void eat() {
		System.out.println("动物具有吃东西的能力");
	}
	public animal() {
		System.out.println("animal 执行了");
	}
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		animal other = (animal) obj;
		if (age != other.age)
			return false;
		if (name == null) {
			if (other.name != null)
				return false;
		} else if (!name.equals(other.name))
			return false;
		return true;
	}
	
}