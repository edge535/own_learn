package test.jv5;
import java.util.*;

public class Pai {
	List<String> suit ;
	String[] suit_symbol = {"♥", "♠", "♣", "♦"};
	String[] suit_number = {"1","2","3","4","5","6","7","8","9","10","J","Q","K"};
	int symbol_index = 0;
	int number_index = 0;
	
	/**
	 * 无参初始化
	 */
	public Pai() {
		suit = new ArrayList<String>();
		add_suit();
	}
	
	/**
	 * 添加一副牌
	 * @param args
	 */
	public void add_suit() {
		 String suit_all;
		 for(int i=0; i<52; i++) {
			 suit_all = add();
			 suit.add(suit_all);
		 }
		 Collections.shuffle(suit); // 打乱list顺序
	}
	
	public String add() {
		String s;
		if(symbol_index<suit_symbol.length) {
			if(number_index<suit_number.length) {
				s = suit_symbol[symbol_index] + suit_number[number_index];
				number_index++;
				return s;
			}else {
				number_index = 0;
				symbol_index++;
				s = suit_symbol[symbol_index] + suit_number[number_index];
				number_index ++;
				return s;
			}
		}else {
			symbol_index = 0;
			s = suit_symbol[symbol_index] + suit_number[number_index];
			number_index++;
			return s;
		}
	}
	
	/**
	 * 显示一整复牌
	 * @param args
	 */
	public void show() {
		int i = 1;
		for(String s : suit) {
			System.out.print("第"+i+"张牌：  ");
			i++;
			System.out.println(s);
		}
	}
	
	
	
	
	public static void main(String[] args) {
		Pai pai = new Pai();
		pai.show();
		System.out.println(pai.suit.get(0));
	}
}
