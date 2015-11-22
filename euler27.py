import primes

#primesmillion = set(primes.primes_alt(1000000))

class QuadraticPrimesFinder:
   def __init__(self, maxprime):
      self.primes = set(primes.primes_alt(maxprime))
      self.highestprime = max(self.primes)

   def isprime(self, num):
      return num in self.primes

   def countprimes(self, a, b):
      count = 0
      current = b
      n = 0
      while self.isprime(current):
         if current > self.highestprime:
            print("Current is too high: a=%s, b=%s, n=%s"%a %b %n)
            raise(RuntimeError)
         n += 1
         count += 1
         current = n*n + a*n + b
      return count

   def producthighestcount(self, maxabs):
      highest = 0
      ahighest = 0
      bhighest = 0
      for a in range(-maxabs,maxabs+1):
         for b in range(maxabs):
            count = self.countprimes(a,b)
            if count > highest:
               highest = count
               ahighest = a
               bhighest = b
      print("a = %s, b = %s, count= %s"%(ahighest, bhighest, highest))
      return ahighest*bhighest

if __name__ == "__main__":
   finder = QuadraticPrimesFinder(1000000)
   print finder.producthighestcount(42)
   print finder.producthighestcount(1000)
