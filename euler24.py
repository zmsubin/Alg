#import fibonacci

def nextfib(lasttwo):
   fib = lasttwo[0] + lasttwo[1]
   return fib

def iseven(num):
   return num % 2 == 0


def euler24(num):
   answer = 0
   lasttwo = [1, 1]
   #n = 3
   fib = nextfib(lasttwo)
   while fib < num:
      temp = list(lasttwo)
      lasttwo[0] = lasttwo[1]
      fib = nextfib(temp)
      lasttwo[1] = fib
      if iseven(fib):
         answer += fib
   return answer
      
