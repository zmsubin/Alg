#include <iostream>


int SumSqMinusSqSum(int num);


int main(int argv, char** argc)
{
   std::cout << "Yomama" << " " << SumSqMinusSqSum(100) << '\n';
}


int SumSqMinusSqSum(int num)
{
   int sumsq = 0;
   int sum = 0;
   for (int i=1; i<num+1; i++) {
      sumsq += i*i;
      sum += i;
   }
   int sqsum = sum*sum;
   return sqsum - sumsq;
}
