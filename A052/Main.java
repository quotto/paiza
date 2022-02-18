package A052;
import java.util.*;

public class Main {
    private static Integer[] slide;
    private static int A;
    private static int B;
    private static int N;
    public static void main(String[] args ) throws Exception {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        A = sc.nextInt();
        B = sc.nextInt();

        slide = new Integer[N];
        Arrays.fill(slide, 0);
        List<Integer> tmp = new ArrayList<>();
        tmp.add(-1);
        while(true) {
            List<Integer> next = new ArrayList<>();
            for(int current: tmp) {
                if(current + A <= N-1) {
                    if(slide[current + A] == 0) {
                        next.add(current + A);
                        slide[current + A] = 1;
                    }
                } else {
                    slide[N-1] = 1;
                }
                if(current + B <= N-1) {
                    if(slide[current + B] == 0) {
                        next.add(current + B);
                        slide[current + B] = 1;
                    }
                } else {
                    slide[N-1] = 1;
                }
            }
            if(next.size() == 0) break;
            tmp = next;
        }

        long result = Arrays.stream(slide).filter(i->i==0).count();
        System.out.println(result);
    }
}