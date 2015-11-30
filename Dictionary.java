import java.util.*;

public class Dictionary<v> {
   
   Integer M; //Number of buckets
   ArrayList<ArrayList<Pair<v>>> data;
   
   public Dictionary (int M) {
      this.M = new Integer(M);
      // Create array of empty lists
      this.data = new ArrayList<ArrayList<Pair<v>>>(M);
      for (int m = 0; m < M; m++) {
          ArrayList<Pair<v>> array = new ArrayList<Pair<v>>();
          this.data.add(array);
      }
   }

   public v search(Integer key) {
      Integer index = hash(key);
      Integer size = data.get(index).size();
      for (int i = 0; i < size; i++) {
         if (data.get(index).get(i).key == key) {
            return data.get(index).get(i).val;
         }
      }
      return null;
   }

   public void insert(Pair<v> pair_in) {
      Integer key = pair_in.key;
      v value = pair_in.val;

      Integer index = hash(key);
      Integer size = data.get(index).size();
      for (int i = 0; i < size; i++) {
         if (data.get(index).get(i).key == key) {
            data.get(index).get(i).val = value;
            return;
         }
      }
      data.get(index).add(pair_in);
   }

   private Integer yomama(Integer int_in) {
       return int_in;
   }

   private Integer hash(Integer int_in) {
      return int_in.hashCode() % M;
   }

   public void Print_table() {
      for (int m = 0; m < M; m++) {
         System.out.println("Entries for index " + m + ";");
         for (int i = 0; i < data.get(m).size(); i++) {
            System.out.println("i = " + i + ": " + data.get(m).get(i).key + ", " + 
                  data.get(m).get(i).val);
         }
      }
   }  
}
