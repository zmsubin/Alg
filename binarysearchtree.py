import sort
import permute




class node:
   def __init__(self, value):
      self.left = None
      self.right = None
      self.value = value

   def retrieve_left(self):
      return self.left

   def retrieve_right(self):
      return self.right

   def add_left(self, node_loc):
      self.left = node_loc

   def add_right(self, node_loc):
      self.right = node_loc

   def retrieve_value(self):
      return self.value


class tree:
   def __init__(self, value):
      self.root = node(value)

   def add_node(self, value, cur_node=None):
      if cur_node == None:
         cur_node = self.root
      cur_value = cur_node.retrieve_value()
      if cur_value == value:
         return
      else:
         if cur_value > value:
            left = cur_node.retrieve_left()
            if not left:
               new_node = node(value)
               cur_node.add_left(new_node)
            else:
               self.add_node(value, left)
         else:
            right = cur_node.retrieve_right()
            if not right:
               new_node = node(value)
               cur_node.add_right(new_node)
            else:
               self.add_node(value, right)

   def print_tree(self, cur_node=None):
      if cur_node == None:
         cur_node = self.root
      left = cur_node.retrieve_left()
      if left:
         self.print_tree(left)
      print(cur_node.retrieve_value())
      right = cur_node.retrieve_right()
      if right:
         self.print_tree(right)

   def in_tree(self, value, cur_node=None):
      if cur_node == None:
         cur_node = self.root
      cur_value = cur_node.retrieve_value()
      if cur_value == value:
         return True
      elif cur_value > value:
         left = cur_node.retrieve_left()
         if not left:
            return False
         else:
            return self.in_tree(value, left)
      else:
         right = cur_node.retrieve_right()
         if not right:
            return False
         else:
            return self.in_tree(value, right)

   @staticmethod
   def new_tree(listin):   
      sorter = sort.mergesort()
      listin_sorted = sorter.msort(listin)
      print listin_sorted
      length = len(listin_sorted)
      pivoti = length/2
      new_tree = tree(listin_sorted[pivoti])
      if pivoti > 0:
         new_tree.add_list_sorted(listin_sorted[:pivoti])
      if pivoti < len(listin_sorted)-1:
         new_tree.add_list_sorted(listin_sorted[pivoti:])
      return new_tree

   def add_list_sorted(self, listin):
      length = len(listin)
      pivoti = length/2
      self.add_node(listin[pivoti])
      if pivoti > 0:
         self.add_list_sorted(listin[:pivoti])
      if pivoti < len(listin)-1:
         self.add_list_sorted(listin[pivoti:])
      
