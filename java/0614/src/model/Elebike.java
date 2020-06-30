package model;

public class Elebike extends Fulei {
	private String eleBand;
	
	public Elebike(String eleBand) {
		super();
		this.setEleBand(eleBand);
	}
	
	protected String getEleBand() {
		return eleBand;
	}

	protected void setEleBand(String eleBand) {
		this.eleBand = eleBand;
	}


	
	public String info() {
		String str = "这是一辆使用"+this.getEleBand()+"牌电池的电动车";
		return str;
	}
}
