package test.jv;
import java.util.*;

public class test_fun {
	//完成 main 方法
    public static void main(String[] args) {
        int[] scores = {89 , -23 , 64 , 91 , 119 , 52 , 73};
        test_fun hello = new test_fun();
        hello.max_3(scores);
        
    }
    
    //定义方法完成成绩排序并输出前三名的功能
    public void max_3(int[] arr){
        Arrays.sort(arr);
        int max_count = 0;
        for(int i=arr.length-1; i>=0; i--){
            if(arr[i]>0 && arr[i]<100){
                System.out.println(arr[i]);
                max_count++;
            }
            if(max_count>=3)
                break;
        }
    }
}
