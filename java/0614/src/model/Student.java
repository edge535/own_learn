package model;

public class Student {
	//成员属性：学号，姓名，性别，年龄,专业
	private String studentNo;
	private String studentName;
	private String studentSex;
	private int studentAge;
	private Subject studentSubject;
	
	//无参构造
	public Student() {
		super();
	}
	
	//多参构造
	public Student(String studentNo, String studentName, String studentSex, int studentAge) {
		super();
		this.setStudentNo(studentNo);
		this.setStudentName(studentName);
		this.setStudentSex(studentSex);
		this.setStudentAge(studentAge);
	}
	public Student(String studentNo, String studentName, String studentSex, int studentAge, Subject studentSubject) {
		super();
		this.setStudentNo(studentNo);
		this.setStudentName(studentName);
		this.setStudentSex(studentSex);
		this.setStudentAge(studentAge);
		this.setStudentSubject(studentSubject);
	}
	/**
	 * 获取专业对象，如果没有实例化，先实例化再返回
	 * @return
	 */
	public Subject getStudentSubject() {
		if(this.studentSubject==null)
			this.studentSubject = new Subject();
		return studentSubject;
	}

	public void setStudentSubject(Subject studentSubject) {
		this.studentSubject = studentSubject;
	}

	public String getStudentNo() {
		return studentNo;
	}
	public void setStudentNo(String studentNo) {
		this.studentNo = studentNo;
	}
	public String getStudentName() {
		return studentName;
	}
	public void setStudentName(String studentName) {
		this.studentName = studentName;
	}
	public String getStudentSex() {
		return studentSex;
	}
	public void setStudentSex(String studentSex) {
		this.studentSex = studentSex;
	}
	public int getStudentAge() {
		return studentAge;
	}
	public void setStudentAge(int studentAge) {
		this.studentAge = studentAge;
	}

	/**
	 * 学生自我介绍
	 * @return 学生的信息 包括姓名，学号，性别，年龄
	 */
	public String info() {
		String str="学生信息如下: \n姓名: "+this.getStudentName()+"\n学号: "+this.getStudentNo()
					+"\n性别: "+this.getStudentSex()+"\n年龄: "+this.getStudentAge();
		return str;
	}
	/**
	 * 学生自我介绍 重载1
	 * @param subjectName
	 * @param subjectLife
	 * @return 学生的信息 包括姓名，学号，性别，年龄, 专业，学制
	 */
	public String introduction(String subjectName,int subjectLife) {
		String str="学生信息如下: \n姓名: "+this.getStudentName()+"\n学号: "+this.getStudentNo()
				+"\n性别: "+this.getStudentSex()+"\n年龄: "+this.getStudentAge()+"\n所报专业名称: "+subjectName
				+"\n 专业年限"+subjectLife;
		return str;
	}
	/**
	 * 学生自我介绍 重载2
	 * @param mySubject
	 * @return 学生的信息 包括姓名，学号，性别，年龄, 专业，学制,编号
	 */
	public String introduction(Subject mySubject) {
		String str="学生信息如下: \n姓名: "+this.getStudentName()+"\n学号: "+this.getStudentNo()
				+"\n性别: "+this.getStudentSex()+"\n年龄: "+this.getStudentAge()+"\n所报专业名称: "+mySubject.getSubjuectName()
				+"\n 专业年限: "+mySubject.getSubjectLife()+"\n 专业编号： "+mySubject.getSubjectNo();
		return str;
	}
	/**
	 * 学生自我介绍 重载3
	 * @return 学生的信息 包括姓名，学号，性别，年龄, 专业，学制,编号
	 */
	public String introduction() {
		String str="学生信息如下: \n姓名: "+this.getStudentName()+"\n学号: "+this.getStudentNo()
				+"\n性别: "+this.getStudentSex()+"\n年龄: "+this.getStudentAge()+"\n所报专业名称: "+this.studentSubject.getSubjuectName()
				+"\n 专业年限: "+this.studentSubject.getSubjectLife()+"\n 专业编号： "+this.studentSubject.getSubjectNo();
		return str;
	}
}
