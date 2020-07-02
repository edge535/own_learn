package runnable;

class PrintRunnable implements Runnable{

	@Override
	public void run() {
		// TODO Auto-generated method stub
		int i=1;
		while(i<=10) {
			System.out.println(Thread.currentThread().getName()+"正在运行"+i++);
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
	}
	
}

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PrintRunnable pr = new PrintRunnable();
		Thread t1 = new Thread(pr);
		t1.start();
		PrintRunnable pr1 = new PrintRunnable();
		Thread t2 = new Thread(pr1);
		t2.start();
	}

}
