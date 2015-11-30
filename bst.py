import sort


class tree:
   def __init__(self):
      self.root = self.node()

   class node:
      def __init__(self, key=None, value=None):
         self.key = key
         self.value = value
         self.left = None
         self.right = None

      def set_value(self, value):
         self.value = value

      def get_value(self):
         return self.value

      def set_left(self, left):
         self.left = left

      def get_left(self):
         return self.left

      def set_right(self, right):
         self.right = right

      def get_right(self):
         return self.right

      def insert(self, key, value):
         if key == self.key:
            return
         elif key < self.key:
            if not self.left:
               self.left = tree.node(key, value)
            else:
               self.left.insert(key, value)
         else:
            if not self.right:
               self.right = tree.node(key, value)
            else:
               self.right.insert(key, value)

      def size(self):
         localsize = 1
         if self.left:
            localsize += self.left.size()
         if self.right:
            localsize += self.right.size()
         return localsize

      def includes_value(self, value):
         if self.get_value() == value:
            return True
         else:
            return not not(self.left and self.left.includes_value(value) or self.right and 
		self.right.includes_value(value))

      def includes_key(self, key):
         if self.key == key:
            return True
         elif key < self.key:
            return not not (self.left and self.left.includes_key(key))
         else:
            return not not (self.right and self.right.includes_key(key))

      def add_list_sorted(self, listin, paired=False):
         length = len(listin)
         pivoti = length/2
         if not paired:
            self.insert(listin[pivoti], listin[pivoti])
         else:
            self.insert(listin[pivoti][0], listin[pivoti][1])
         if pivoti > 0:
            self.add_list_sorted(listin[:pivoti], paired)
         if pivoti < len(listin)-1:
            self.add_list_sorted(listin[pivoti:], paired)

      def get_value_at(self, key):
         if self.key == key:
            return self.get_value()
         elif self.key > key:
            return (self.left and self.left.get_value_at(key))
         else:
            return (self.right and self.right.get_value_at(key))

      def print_subtree(self):
         if self.left:
            self.left.print_subtree()
         print self.get_value()
         if self.right:
            self.right.print_subtree()
      
   @staticmethod
   def new_tree(listin, paired=False):
      sorter = sort.mergesort()
      listin_sorted = sorter.msort(listin)
      print listin_sorted
      length = len(listin_sorted)
      pivoti = length/2
      new_tree = tree()
      if not paired:
         new_tree.root.key = listin_sorted[pivoti]
         new_tree.root.set_value(listin_sorted[pivoti])
      else:
         new_tree.root.key = listin_sorted[pivoti][0]
         new_tree.root.set_value(listin_sorted[pivoti][1])
      if pivoti > 0:
         new_tree.root.add_list_sorted(listin_sorted[:pivoti], paired)
      if pivoti < len(listin_sorted)-1:
         new_tree.root.add_list_sorted(listin_sorted[pivoti:], paired)
      return new_tree


   def size(self):
      return self.root.size()

   def includes_value(self, value):
      return self.root.includes_value(value)

   def includes_key(self, key):
      return self.root.includes_key(key)


