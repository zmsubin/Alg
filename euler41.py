import primes
import permute

maxsearch = 40000
class PandigitalPrimeFinder:
   def __init__(self):
      self.primelist = primes.primes_alt(maxsearch)
      self.primeset = set(self.primelist)
   
   def is_prime(self, num):
      if num < maxsearch:
         return num in self.primeset
      else:
         for p in self.primelist:
            if num % p == 0:
                return False
      return True

   def largest_pandigital_prime(self):
      perm = permute.permutor()
      perm.permute(list('7654321'))#('987654321'))
      #plist = perm.b
      
      print int("".join(perm.b[0]))
      print len(perm.b)
      for plist in perm.b:
         num = int("".join(plist))
         if self.is_prime(num):
            return num

if __name__ == '__main__':
   finder = PandigitalPrimeFinder()
   print finder.largest_pandigital_prime()
   print finder.is_prime(1299709)
