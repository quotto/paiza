import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;
import java.util.stream.Collectors;

public class App {
  public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      String[] params = scanner.nextLine().split(" ");
      int N = Integer.parseInt(params[0]);
      int Q = Integer.parseInt(params[1]);

      // 年齢計算用のテーブルをnullで初期化(N * N)
      Integer[][] calcTable = new Integer[N][N];
      Integer[] ageTable = new Integer[N];
      for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
          calcTable[i][j] = null;
        }
        ageTable[i] = null;
      }

      // 回答をすべて年齢計算用テーブルに格納する
      for(int q=0; q<Q; q++) {
        String[] lines = scanner.nextLine().split(" ");
        int person = Integer.parseInt(lines[0]);
        int target = Integer.parseInt(lines[1]);
        int diff = Integer.parseInt(lines[2]);
        // 回答者が対象者より番号が上の場合は差分を反転する
        diff = person > target ? diff * -1 : diff;

        // 必ず番号が小さい村人のテーブルに入れる
        Integer previous_diff =  calcTable[Math.min(person,target)-1][Math.max(person,target)-1];
        if(!Objects.isNull(previous_diff)) {
          // 既に値が存在し年齢差が一致しない場合は回答に矛盾がある
          if(previous_diff != diff) {
            System.out.println(-1);
            return;
          }
        } else {
          calcTable[Math.min(person,target)-1][Math.max(person,target)-1] = diff;
        }
      }

      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          Integer diff = calcTable[i][j];
          if (!Objects.isNull(diff)) {
            boolean isnullPerson = Objects.isNull(ageTable[i]);
            boolean isnullTarget = Objects.isNull(ageTable[j]);
            if (isnullPerson && isnullTarget) {
              ageTable[i] = 0;
              ageTable[j] = diff;
            } else if (!isnullPerson && isnullTarget) {
              ageTable[j] = ageTable[i] + diff;
            } else if (isnullPerson && !isnullTarget) {
              ageTable[i] = ageTable[j] + (diff * -1);
            } else {
              int previous_target = ageTable[j];
              ageTable[j] = ageTable[i] + diff;
              if (previous_target != ageTable[j]) {
                // 修正前後の年齢にに矛盾があれば不正な回答があったとみなして終了
                System.out.println(-1);
                return;
              }
            }
          }
        }
      }

      for(int i=0; i< N; i++){
        if(!Objects.isNull(ageTable[i])) {
          System.out.println(i+":"+ageTable[i]);
        }
      }
      List<Integer> resultList = Arrays.asList(ageTable).stream().filter(v->!Objects.isNull(v)).collect(Collectors.toList());
      Integer max = resultList.stream().max(Comparator.naturalOrder()).get();
      Integer min = resultList.stream().min(Comparator.naturalOrder()).get();
      if(min < 0) {
        max += Math.abs(min);
        min += Math.abs(min);
      }
      if(max > 100) {
        min -= (100 - max);
        max -= (100 - max);
      }
      if(max > 100 || min < 0) {
        System.out.println(-1);
      } else {
        System.out.println(max - min);
      }
  }
}