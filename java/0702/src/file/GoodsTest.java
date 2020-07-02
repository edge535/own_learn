package file;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class GoodsTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Goods goods1 = new Goods("Gd001","电脑",30000);
		try {
			FileOutputStream fos = new FileOutputStream("imooc.txt");
			ObjectOutputStream oos = new ObjectOutputStream(fos);
			FileInputStream fis = new FileInputStream("imooc.txt");
			ObjectInputStream ois = new ObjectInputStream(fis);
			//将对象信息写入文件
			oos.writeObject(goods1);
			oos.writeBoolean(true);
			oos.flush();
			//读取对象文件
			try {
				Goods goods2 = (Goods) ois.readObject();
				System.out.println(goods2);
				
			} catch (ClassNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			boolean b = ois.readBoolean();
			System.out.println(b);
			fos.close();
			oos.close();
			fis.close();
			ois.close();
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
