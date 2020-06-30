package CatSort;

import java.util.Comparator;

public class AgeComparator implements Comparator<Cat> {

	@Override
	public int compare(Cat o1, Cat o2) {
		// TODO Auto-generated method stub
		int age1 = o1.getMonth();
		int age2 = o2.getMonth();
		return age2-age1;
	}

}
