package test.jv4;

import java.util.Comparator;

public class studentComparator implements Comparator<student> {

	@Override
	public int compare(student arg0, student arg1) {
		// TODO Auto-generated method stub
		return arg0.name.compareTo(arg1.name);
	}

}
