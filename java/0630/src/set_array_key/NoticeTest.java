package set_array_key;

import java.util.ArrayList;
import java.util.Date;

public class NoticeTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Notice notice1 = new Notice(1,"欢迎来到慕课网！","管理员",new Date());
		Notice notice2 = new Notice(2,"请同学们按时提交作业！","老师",new Date());
		Notice notice3 = new Notice(3,"考勤通知！","老师",new Date());
		
		//添加公告
		ArrayList noticeList = new ArrayList();
		noticeList.add(notice1);
		noticeList.add(notice2);
		noticeList.add(notice3);
		
		//显示公告
		System.out.println("公告的内容为：");
		for(int i=0; i<noticeList.size(); i++) {
			System.out.println(i+1+":"+((Notice)(noticeList.get(i))).getTitle());
		}
		
		//在第一条公告后添加一个新公告
		Notice notice4 = new Notice(4,"在线编辑器可以使用了","管理员",new Date());
		noticeList.add(1, notice4);
		System.out.println("添加后公告的内容为：");
		for(int i=0; i<noticeList.size(); i++) {
			System.out.println(i+1+":"+((Notice)(noticeList.get(i))).getTitle());
		}
		
		//删除按时完成作业
		noticeList.remove(2);
		System.out.println("删除后公告的内容为：");
		for(int i=0; i<noticeList.size(); i++) {
			System.out.println(i+1+":"+((Notice)(noticeList.get(i))).getTitle());
		}
		
		//修改第二条公告中的标题
		notice4.setTitle("JAVA在线编辑器可以使用了！");
		System.out.println("修改后公告的内容为：");
		for(int i=0; i<noticeList.size(); i++) {
			System.out.println(i+1+":"+((Notice)(noticeList.get(i))).getTitle());
		}
		
		
	}

}
