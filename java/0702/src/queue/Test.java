package queue;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Queue queue = new Queue();
		new Thread(new producer(queue)).start();
		new Thread(new Customer(queue)).start();
	}	

}
