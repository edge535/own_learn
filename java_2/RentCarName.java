package test.jv2;

public class RentCarName {
	private String[] carName = {"�µ�A4", "���Դ�6", "Ƥ��ѩ6", "��      ��", "�ɻ���", "��ά��"};
	public String getName(int index) {
		if(index<=carName.length)
			return carName[index-1];
		else
			return "Not this car!";
	}

}
