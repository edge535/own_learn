package test.jv;

public class Telphone {
	private float screen;
	private float cpu;
	private float mem;
	int var; // 会给成员变量自动初始值

	public float getScreen() {
		return screen;
	}
	
	public void setScreen(float new_screen) {
		screen = new_screen;
	}

	public float getCpu() {
		return cpu;
	}

	public void setCpu(float cpu) {
		this.cpu = cpu;
	}

	public float getMem() {
		return mem;
	}

	public void setMem(float mem) {
		this.mem = mem;
	}

	public Telphone(){ 
		System.out.println("无参的构造方法"); 
	}

	public Telphone(float screen, float cpu, float mem) {
		System.out.println("有参的构造方法");
		screen = screen;
		cpu = cpu;
		mem = mem;
	}

	void call() {
		int localvar = 0; // 局部变量不自动给与初始值
		System.out.println("localvar:" + localvar);
		System.out.println("var:" + var);
		System.out.println("Telphone有打电话的功能");
	}

	void sendMessage() {
		System.out.println("SCREEN:" + screen + " CPU:" + cpu + " MEM:" + mem + "Telphone有发短信的功能");
	}

}