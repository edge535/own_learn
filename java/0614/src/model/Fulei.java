package model;

public class Fulei {
	protected String band;
	protected String color;
	protected int lunzi=2;
	protected int zuoyi=1;
	
	//无参构造器
	public Fulei() {
		this.setBand("天宇牌");
		this.setColor("红色");
		this.setLunzi(4);
		this.setZuoyi(2);
	}
	//两个参数的构造器
	public Fulei(String band, String color) {
		this.setBand(band);
		this.setColor(color);
	}
	//全部参数的构造器
	public Fulei(String band, String color, int lunzi, int zuoyi) {
		super();
		if(band == null)
			band = "天宇牌";
		if(color == null)
			color = "红色";
		if(lunzi == 0)
			lunzi=4;
		if(zuoyi == 0)
			zuoyi=2;
		this.setBand(band);
		this.setColor(color);
		this.setLunzi(lunzi);
		this.setZuoyi(zuoyi);
	}
	protected String getBand() {
		return band;
	}
	protected void setBand(String band) {
		this.band = band;
	}
	protected String getColor() {
		return color;
	}
	protected void setColor(String color) {
		this.color = color;
	}
	protected int getLunzi() {
		return lunzi;
	}
	protected void setLunzi(int lunzi) {
		this.lunzi = lunzi;
	}
	protected int getZuoyi() {
		return zuoyi;
	}
	protected void setZuoyi(int zuoyi) {
		this.zuoyi = zuoyi;
	}
	
	public String info() {
		String str = "这是一辆"+this.getColor()+"颜色的,"+this.getBand()+"牌的非机动车"
				+",有"+this.getLunzi()+"个轮子"+",有"+this.getZuoyi()+"个座椅的非机动车";
		return str;
	}
	
	
}
