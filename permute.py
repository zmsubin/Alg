class permutor:
   def __init__(self):
      self.b = []

   def permute(self,a,aa=[]):
      if len(a) == 1:
        bb = aa + a
        self.b.append(bb)
      else:
         #print a
         for i in range(len(a)):
            #print i
            bb = list(aa)
            bb.append(a[i])
            a1 = list(a)
            a1.pop(i)
            self.permute(a1, bb)

