import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Hamming_Distance {
    public static void main(String[] args) {
        int yes_no;



        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the No. of code words :");
        int no_of_codewords = sc.nextInt();
        System.out.print("Enter the length of each codeword :");
        int length_of_codewords = sc.nextInt();
        String[] arr = new String[no_of_codewords];
//        re_start: {
//        int count = 1;
//        while(count<=no_of_codewords) {
            for (int i = 0; i < no_of_codewords; i++) {
                System.out.print("Enter the code word" + i + " :");
                String temp_data = sc.next();
                if (temp_data.length() == length_of_codewords) {
                    arr[i] = temp_data;
                } else {
                    System.out.println("Data length should be" + length_of_codewords + ".");
                    break;
                }
            }
//            count++;
//            System.out.println("Do you want to restart? 1->YES | 2->NO");
//            yes_no = sc.nextInt();
//        }while (yes_no != 0);

//        for()
        int ans = getMinimum(arr);
        System.out.println("Hamming distance :" +ans);
    }
    public static int getMinimum(String[] arr){
        int min = 0;
        for(int i=0;i<arr.length;i++){
            for (int j=i+1;j< arr.length;j++) {
                if (arr.length % 2 != 0 && i + 1 == arr.length - 1) break;
                int dis = getHammingDistance(arr[i], arr[j]);
                if (min > dis && min !=0) min = dis;
            }
        }
        return min;
    }
    public static int getHammingDistance(String s1, String s2) {
        if (s1.length() != s2.length()) {
            throw new IllegalArgumentException("The two strings must be the same length");
        }

        int hammingDistance = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                hammingDistance++;
            }
        }
        return hammingDistance;
    }
}