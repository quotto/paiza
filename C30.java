import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

class C30{
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Integer[] HW = Arrays.asList(sc.nextLine().split(" ")).stream().mapToInt(Integer::parseInt).toArray();
        List<List<String>> result = new ArrayList<>();
        for(int h=0; h<HW[0]; h++) {
            List<String> list = Arrays.asList(sc.nextLine().split(" ", -1));
            result.add(list.stream().map(s->new Integer(s) >=128 ? "1" : "0").collect(Collectors.toList()));
        }
        result.forEach(l->System.out.println(String.join(" ", l)));
    }
}