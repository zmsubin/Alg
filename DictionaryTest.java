import java.util.*;
//import math.*;

public class DictionaryTest {


    public static void main(String[] args) {
        Dictionary<Double> dict = new Dictionary<Double>(17);
        for (Integer i = 0; i < 100; i++) {
            Double val = Math.pow(3.1415,i%29);
            Pair<Double> pair = new Pair(i, val);
            dict.insert(pair);
        }
        dict.Print_table();    
        System.out.println(dict.search(50));
        System.out.println(dict.search(100));
    }

}
