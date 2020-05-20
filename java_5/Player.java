package test.jv5;

public class Player {
	int id;
	String name;
	String[] hold;
	String sym;
	int sym_num;
	
	/**
	 * 初始化
	 */
	public void init(int id, String name) {
		this.id = id;
		this.name = name;
		hold = new String[2];
	}
	
	/**
	 * 获取两张手牌中大的那张
	 * @return
	 */
	public int get_max() {
		int one=0;
		int two=0;
		if( !(hold[0].substring(1).equals("J")) && !(hold[0].substring(1).equals("Q")) && !(hold[0].substring(1).equals("K")) ) {
			one = Integer.parseInt(hold[0].substring(1));
		}else{
			switch(hold[0].substring(1)) {
				case "J":
					one = 11;
					break;
				case "Q":
					one = 12;
					break;
				case "K":
					one = 13;
					break;
			}
		}
		if( !(hold[1].substring(1).equals("J")) && !(hold[1].substring(1).equals("Q")) && !(hold[1].substring(1).equals("K")) ) {
			two = Integer.parseInt(hold[1].substring(1));
		}else {
			switch(hold[1].substring(1)) {
				case "J":
					two = 11;
					break;
				case "Q":
					two = 12;
					break;
				case "K":
					two = 13;
					break;
			}
		}
		if(one>two) {
			sym = hold[0].substring(0,1);
			return one;
		}else if(two>one) {
			sym = hold[1].substring(0,1);
			return two;
		}else if(two == one) {
			String one_sym ="",  two_sym="";
			int one_int=0, two_int=0;
			one_sym = hold[0].substring(0,1);
			switch(one_sym) {
				case "♥":
					one_int = 40;
				case "♠":
					one_int = 30;
				case "♣":
					one_int = 20;
				case "♦":
					one_int = 10;
			}
			two_sym = hold[1].substring(0,1);
			switch(two_sym) {
				case "♥":
					two_int = 40;
				case "♠":
					two_int = 30;
				case "♣":
					two_int = 20;
				case "♦":
					two_int = 10;
			}
			if(one_int>=two_int) {
				sym_num = one_int;
				sym = one_sym;
			}else {
				sym_num = two_int;
				sym = two_sym;
			}
				
			return one;
		}
		return -1;
	}

	
	@Override
	public String toString() {
		return "Player [id=" + id + ", name=" + name + "]";
	}
	
	public void end() {
		System.out.println("["+hold[0]+","+hold[1]+"]");
	}

	public static void main(String[] args) {
		Player p = new Player();
		p.init(1,"Anna");
		p.hold[0] = "♥2";
		p.hold[1] = "♦Q";
		System.out.println(p.get_max());
		System.out.println(p.sym);
		System.out.println(p.sym_num);
		p.end();
	}
}
