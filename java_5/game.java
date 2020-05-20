package test.jv5;
import java.util.Scanner;

public class game {
	Player[] p = {new Player(),new Player()};
	Scanner input = new Scanner(System.in);
	boolean id_cf = true; // 当id输入有误是为true
	int id = 0;
	StringBuilder name = new StringBuilder();
	Pai pai = new Pai();
	
	
	public static void main(String[] args) {
		game g = new game();
		g.input_id_name();
		System.out.println("系统提示->: 玩家初始化完毕，开始发牌");
		g.deal();
		g.p[0].end();g.p[1].end();
		System.out.println("系统提示->: 正在进行游戏，请稍后");
		Player win = g.play();
		System.out.println("系统提示->: 本局胜利者为"+win.name+"! 他的手牌是：");
		win.end();
	}


	
	/**
	 * id和name的输入及异常处理
	 * @param num
	 * @param id
	 */
	public int input_id(int num) {
		id_cf = true; //避免二号玩家因为一号玩家正确设置而无法进入循环
		while(id_cf) {
			try {
				input = new Scanner(System.in);
				System.out.println("系统提示->: 输入"+num+"号玩家的ID：");
				id_cf = false; //id正确输入则设置为false
				return input.nextInt();
			} catch (Exception e) {
				id_cf = true; //输入有误保持true
				input = new Scanner(System.in);
				System.out.println("系统提示->: ID只能是数字");
			}
		}
		return -1;
	}
	public void input_name(int num, StringBuilder name) {
		input = new Scanner(System.in);
		System.out.println("系统提示->: 输入"+num+"号玩家的名字：");
		name.delete(0, name.length());
		name.append(input.next());
	}
	public void input_id_name() {
		for(int i=0; i<2; i++) {
			id = input_id(i+1);
			input_name(i+1,name);
			p[i].init(id,name.toString());
		}
		System.out.println("系统提示->: -----------");
	}
	
	/**发牌
	 * 
	 */
	public void deal() {
		System.out.println("	:玩家"+p[0].name+"手牌+1");
		p[0].hold[0] = pai.suit.get(0);
		System.out.println("	:玩家"+p[1].name+"手牌+1");
		p[1].hold[0] = pai.suit.get(1);
		System.out.println("	:玩家"+p[0].name+"手牌+1");
		p[0].hold[1] = pai.suit.get(2);
		System.out.println("	:玩家"+p[1].name+"手牌+1");
		p[1].hold[1] = pai.suit.get(3);
		System.out.println("系统提示->:发牌完毕");
		System.out.println("系统提示->: -----------");
	}
	
	/**
	 * 比较和结果
	 *
	 */
	public Player play() {
		if(p[0].get_max() > p[1].get_max()) {
			return p[0];
		}else if(p[0].get_max() < p[1].get_max()) {
			return p[1];
		}else {
			if(p[0].sym_num > p[1].sym_num)
				return p[0];
			else
				return p[1];
		}
	}

	
	
}
