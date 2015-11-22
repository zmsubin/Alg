def insertsort(listin):
   for i in range(1,len(listin)):
      key = listin[i-1]
      for j in range(i,len(listin)):
         if listin[j] < key:
            listin = insert(listin, i-1,j)
   return listin


def insertsortrev(listin):
   for i in range(1,len(listin)):
      key = listin[i-1]
      for j in range(i,len(listin)):
         if listin[j] > key:
            listin = insert(listin, i-1,j)
   return listin


def bubblesort(lst):
   for i in range(len(lst)):
      for j in reversed(range(i+1,len(lst))):
         if lst[j] < lst[j-1]:
            lst = swap(lst,j-1,j)
   return lst


def insert(lst,a,b):
   if a>=b:
      raise(RuntimeError)
   for j in range(b-a):
      jj = b-j-1
      lst = swap(lst,jj,jj+1)
   return lst

def swap(lst,a,b):
   temp = lst[a]
   lst[a] = lst[b]
   lst[b] = temp
   return lst

class a:
   def __init__(self, arr):
      self.arr = arr
      self.l = len(arr)

   def swap(self,a,b):
      temp = self.arr[a]
      self.arr[a] = self.arr[b]
      self.arr[b] = temp
 
   def bubblesort(self):
      for i in range(self.l):
         for j in reversed(range(i+1,self.l)):
            if self.arr[j] < self.arr[j-1]:
               self.swap(j-1,j)


class mergesort:
   #def __init__(self, a):
   #    self.a = a

   @staticmethod
   def msort(a):
      if (len(a) == 1):
         return a
      else:
         mid = len(a)/2
         a1 = mergesort.msort(a[:mid])
         a2 = mergesort.msort(a[mid:])
         return mergesort.zzip(a1, a2)

   @staticmethod
   def zzip(a1, a2):
      a1l = len(a1)
      a2l = len(a2)
      b = [None] * (a1l + a2l)
      a1j = 0
      a2j = 0
      k = 0
      while a1j < a1l or a2j < a2l:
         if a1j == a1l:
             b[k] = a2[a2j]
             k += 1
             a2j += 1
         elif a2j == a2l:
             b[k] = a1[a1j]
             k += 1
             a1j += 1
         else:
             if a1[a1j] < a2[a2j]:
                b[k] = a1[a1j]
                k += 1
                a1j += 1
             else:
                b[k] = a2[a2j]
                k += 1
                a2j += 1
      return b
