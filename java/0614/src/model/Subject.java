package model;

public class Subject {
	// 学科名称，学科编号，学制年限,报名选修的学生信息，报名选修的学生个数
	private String subjectName;
	private String subjectNo;
	private int subjectLife;
	private Student[] myStudents;
	private int studentNum;

	// 无参构造
	public Subject() {
	}

	// 有参构造,实现对名称，编号，年限的赋值
	public Subject(String subjectName, String subjectNo, int sunjectLife) {
		this.setSubjuectName(subjectName);
		this.setSubjectNo(subjectNo);
		this.setSubjectLife(sunjectLife);
	}
	
	// 有参构造,实现对全部属性的赋值
	public Subject(String subjectName, String subjectNo, int sunjectLife,Student[] myStudents) {
		this.setSubjuectName(subjectName);
		this.setSubjectNo(subjectNo);
		this.setSubjectLife(sunjectLife);
		this.setMyStudents(myStudents);
	}

	public int getStudentNum() {
		return studentNum;
	}

	public void setStudentNum(int studentNum) {
		this.studentNum = studentNum;
	}

	/*
	 * 获取选修专业的学生信息，如果学生信息的数组未被初始化，则先初始化长度为200
	 */
	public Student[] getMyStudents() {
		if(this.myStudents==null)
			this.myStudents=new Student[200];
		return myStudents;
	}

	public void setMyStudents(Student[] myStudents) {
		this.myStudents = myStudents;
	}

	public void setSubjuectName(String subjectName) {
		this.subjectName = subjectName;
	}

	public String getSubjuectName() {
		return this.subjectName;
	}

	public String getSubjectNo() {
		return subjectNo;
	}

	public void setSubjectNo(String subjectNo) {
		this.subjectNo = subjectNo;
	}

	public int getSubjectLife() {
		return subjectLife;
	}

	public void setSubjectLife(int subjectLife) {
		if (subjectLife <= 0)
			return;
		this.subjectLife = subjectLife;
	}

	/**
	 * 专业介绍的方法
	 * @return 专业介绍的相关信息，包括 名称，编号，年限
	 */
	public String info() {
		String str = "专业信息如下:\n 专业名称: " + this.getSubjuectName() + 
				"\n 专业编号: " + this.getSubjectNo() + 
				"\n 专业学制: "+ this.getSubjectLife() + "年";
		return str;
	}
	
	public void addStudent(Student stu) {
		/**
		 * 1.将学生保存到数组中
		 * 2.将学生个数保存到studentNum
		 */
		//1.
		int i;
		for(i=0;i<this.getMyStudents().length;i++) {
			if(this.getMyStudents()[i]==null) {
				stu.setStudentSubject(this);
				this.getMyStudents()[i]=stu;
				break;
			}	
		}
		//2.
		this.studentNum=i+1;
	}
	
	
}
