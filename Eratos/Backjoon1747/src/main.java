import java.util.ArrayList;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        // ArrayList로 구현
        ArrayList<Boolean> primeList;

        // 사용자로부터의 콘솔 입력
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();

        int n = 2000000;
        // n <= 1 일 때 종료
        if(n <= 1) return;

        // n+1만큼 할당
        primeList = new ArrayList<Boolean>(2000000);
        // 0번째와 1번째를 소수 아님으로 처리
        primeList.add(false);
        primeList.add(false);
        // 2~ n 까지 소수로 설정
        for(int i=2; i<=n; i++ )
            primeList.add(i, true);

        // 2 부터  ~ i*i <= n
        // 각각의 배수들을 지워간다.
        for(int i=2; (i*i)<=n; i++){
            if(primeList.get(i)){
                for(int j = i*2; j<=n; j+=i) primeList.set(j, false);
                //i*i 미만은 이미 처리되었으므로 j의 시작값은 i*i로 최적화할 수 있다.
            }
        }

        for(int s = N; s<2000000; s++){
            boolean flag = true;
            if(primeList.get(s)) {
                int length = (int) (Math.log10(s) + 1);
                int half;
                if(length==1)
                    half = length;
                half = length / 2;
                int q = length-1;
                String sStr = Integer.toString(s);

                for (int k = 0; k < half; k++) {
                    int a = (sStr.charAt(k));
                    int b = (sStr.charAt(q));
                    if (a != b) {
                        flag = false;
                    }
                    q--;
                }
            }
            if (primeList.get(s) && flag == true) {
                System.out.println(s);
                break;
            }
        }

    }
}
