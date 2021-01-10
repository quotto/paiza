package track;
import java.util.Scanner;
import java.util.Map.Entry;
import java.util.regex.Pattern;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class App {
  
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    List<String> words = new ArrayList<>(Arrays.asList(scanner.nextLine().split(" ")));

    // 最後の値を対象数値として取り出す
    int target = Integer.parseInt(words.remove(words.size()-1));

    // 割り切れる数字と文字列の組み合わせを結果として保存
    HashMap<Integer,String> result = new HashMap<>();
    words.forEach((s)->{
        String[] pair = s.split(":");
        Integer key = new Integer(pair[0]);
        if((target % key) == 0) {
            result.put(key,pair[1]);
        }
    });

    if(result.size() > 0) {
        // キーの昇順でソートして出力する
        result.entrySet().stream().sorted(Entry.comparingByKey()).forEach(e -> {
            System.out.print(e.getValue());
        });
        System.out.println();
    } else {
        // 結果が空なら対象の数字をそのまま出力
        System.out.println(target);
    }
  }
}
