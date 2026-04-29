# Реализация деревьев и heap sort
class Node:
  def __init__ (self, item):
    self.value = item
    self.right = None
    self.left = None
  def new_right (self, item):
    self.right = Node (item)
  def new_left (self, item):
    self.left = Node (item)

def new_node_bst (node:Node, item):
  if item < node.value:
    if node.left == None:
      node.new_left (item)
    else:
      node.left = new_node_bst (node.left, item)
  elif item > node.value:
    if node.right == None:
      node.new_right (item)
    else:
      node.right = new_node_bst (node.right, item)
  return node

def search_node_bst (node:Node, item):
  if item == node.value:
    return str (node.value)
  elif item < node.value:
    if node.left == None:
      return '\nЧисло не найдено'
    else:
      return str (node.left.value) + '\\' + search_node_bst (node.left, item)
  elif item > node.value:
    if node.right == None:
      return '\nЧисло не найдено'
    else:
      return str (node.right.value) + '\\' + search_node_bst (node.right, item)

class BST:
  def __init__ (self):
    self.root = None

  def new_node (self, item):
    if self.root == None:
      self.root = Node (item)
    else:
      self.root = new_node_bst (self.root, item)

  def search_nod (self, item):
    if self.root == None:
      return 'Бинарное дерево пусто'
    else:
      path = '\\' + search_node_bst (self.root, item)
