package test.jv;

public class Telphone {
	private float screen;
	private float cpu;
	private float mem;
	int var; // �����Ա�����Զ���ʼֵ

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
		System.out.println("�޲εĹ��췽��"); 
	}

	public Telphone(float screen, float cpu, float mem) {
		System.out.println("�вεĹ��췽��");
		screen = screen;
		cpu = cpu;
		mem = mem;
	}

	void call() {
		int localvar = 0; // �ֲ��������Զ������ʼֵ
		System.out.println("localvar:" + localvar);
		System.out.println("var:" + var);
		System.out.println("Telphone�д�绰�Ĺ���");
	}

	void sendMessage() {
		System.out.println("SCREEN:" + screen + " CPU:" + cpu + " MEM:" + mem + "Telphone�з����ŵĹ���");
	}

}