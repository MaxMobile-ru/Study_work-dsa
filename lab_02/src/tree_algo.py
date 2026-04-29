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
        self.new_nod (self.right, item)
    elif item < self.root:
      if self.left == None:
        self.left = item
      else:
        self.new_nod (self.left, item)

  def search_nod (self, item, path='\\'):
    if self.root == item:
      return path + str (item)
    elif item < self.root:
      return self.search_nod (self.left, item, path + str (item) + '\\')
    elif item > self.root:
      return self.search_nod (self.right, item, path + str (item) + '\\')
