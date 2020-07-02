package file;

import java.io.File;

public class FileDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//创建对象
		//File file1 = new File("D:\\eclipse_java_project"\\score.txt");
		//File file1 = new File("D:\\eclipse_java_project","0702\\score.txt");
		File file = new File("D:\\eclipse_java_project");
		File file1 = new File(file,"0702\\score.txt");
		//判断是文件还是路径
		System.out.println("是否是目录"+file1.isDirectory());
		System.out.println("是否是文件"+file1.isFile());
		//创建文件
		File file2 = new File("D:\\eclipse_java_project\\0702","NewTest");
		if(!file2.exists()) {
			file2.mkdir();
		}
		File file3 = new File("D:\\eclipse_java_project\\0702","NewTest2\\test");
		if(!file3.exists()) {
			file3.mkdirs();
		}
	}

}
