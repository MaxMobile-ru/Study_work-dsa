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



class BST:
  def __init__ (self):
    self.root = None

  def new_nod (self, item):
    if self.root == None:
      self.root = Node (item)
    else:
      self.root = new_node_bst (self.root, item)
