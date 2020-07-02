package queue;

public class producer implements Runnable {
	Queue queue;
	producer(Queue queue){
		this.queue = queue;
	}

	@Override
	public void run() {
		// TODO Auto-generated method stub
		int i=0;
		while(true) {
			queue.set(i++);
			try {
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

}
