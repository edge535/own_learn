package test.jv2;

public class RentCarName {
	private String[] carName = {"奥迪A4", "马自达6", "皮卡雪6", "金      龙", "松花江", "依维柯"};
	public String getName(int index) {
		if(index<=carName.length)
			return carName[index-1];
		else
			return "Not this car!";
	}

}
