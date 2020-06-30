package set_array_key;

import java.util.Date;

public class Notice {
	private int id;
	private String  title;
	private String createor;
	private Date creaTime;
	public Notice(int id, String title, String createor, Date creaTime) {
		super();
		this.id = id;
		this.title = title;
		this.createor = createor;
		this.creaTime = creaTime;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getCreateor() {
		return createor;
	}
	public void setCreateor(String createor) {
		this.createor = createor;
	}
	public Date getCreaTime() {
		return creaTime;
	}
	public void setCreaTime(Date creaTime) {
		this.creaTime = creaTime;
	}
	
}
