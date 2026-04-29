# Реализация деревьев и heap sort
class BST:
  def __init__ (self):
    self.root = None
    self.right = None
    self.left = None

  def new_nod (self, item):
    if self.root == None:
      self.root = item
    elif item > self.root:
      if self.right == None:
        self.right = item
      else:
        self.right.new_nod (item)
    elif item < self.root:
      if self.left == None:
        self.left = item
      else:
        self.left.new_nod (item)

  def search_nod (self, item, path='\\'):
    if self.root == item:
      return path + str (item)
    elif item < self.root:
      return self.left.search_nod (item, path + str (item) + '\\')
    elif item > self.root:
      return self.right.search_nod (item, path + str (item) + '\\')
