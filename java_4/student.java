package test.jv4;
import java.util.*;

public class student implements Comparable<student> {
	public String id;
	public String name;
	public Set<course> sourses;
	
	public student(String id, String name) {
		this.id = id;
		this.name = name;
		this.sourses = new HashSet<course>();
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((name == null) ? 0 : name.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!(obj instanceof student))
			return false;
		student other = (student) obj;
		if (name == null) {
			if (other.name != null)
				return false;
		} else if (!name.equals(other.name))
			return false;
		return true;
	}
	
	@Override
	public int compareTo(student o) {
		return this.id.compareTo(o.id);
	}
}
