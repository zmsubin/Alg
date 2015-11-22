import java.util.*;

public class Primes {
   public static void main(String[] args) {
      ArrayList<Integer> answer = Primes.primes_calculator(1000000);
      System.out.println(answer.get(10000));
   }

   public static ArrayList<Integer>primes_calculator(Integer num) {//ArrayList<Integer> primes_calculator(Integer num) {
      //Integer[] array;
      ArrayList<Integer> array = new ArrayList<Integer>();
      for (Integer i=2; i<=num; i++) {
         array.add(i);
      }
      HashSet<Integer> candidates = new HashSet<Integer>();
      for (Integer i=0; i<array.size(); i++) {
         candidates.add(array.get(i));
      }
      for (Integer i=0; i<array.size(); i++) {
         if (i%1000==0) {System.out.println(i);}
         Integer cur = array.get(i);
         if (candidates.contains(cur)) {
            for (Integer j=2; j<num/cur+1; j++) {
               if (candidates.contains(j*cur)) {candidates.remove(j*cur);}
            }
         }
      }
      ArrayList<Integer> arrayout;
      //arrayout = new Integer[candidates.size()];
      //for (Integer i=0; arrayout.size(); i++)
         //arrayout[i] = candidates[i];
      arrayout = new ArrayList<Integer>(candidates);
      Collections.sort(arrayout);
      return arrayout;
   }
}
