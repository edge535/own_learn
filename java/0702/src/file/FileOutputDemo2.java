package file;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class FileOutputDemo2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			FileInputStream fis = new FileInputStream("2.gif");
			FileOutputStream fos = new FileOutputStream("2copy.gif");
			int n=0;
			byte[] b = new byte[1024];
			while((n=fis.read(b))!=-1) {
				fos.write(b,0,n);
			}
			
			fis.close();
			fos.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
