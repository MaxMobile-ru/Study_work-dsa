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
      return '-1'
    else:
      return str (node.value) + '(left)' + '\\' + search_node_bst (node.left, item)
  elif item > node.value:
    if node.right == None:
      return '-1'
    else:
      return str (node.value) + '(right)' + '\\' + search_node_bst (node.right, item)

def func_del_node_bst (node:Node, item):
  if node.value == item:
    node.value = None
    if node.left == None and node.right == None:
      return node
    else:
      node.value = find_replacer (node.left)
  elif item < node.value:
    node.left = func_del_node_bst (node.left, item)
  elif item > node.value:
    node.right = func_del_node_bst (node.right, item)
  return node

def find_replacer (node:Node):
  if node.left == None and node.right == None:
    res = node.value
    node.value = None
    return res
  else:
    return find_replacer (node.right)

class BST:
  def __init__ (self):
    self.root = None

  def new_node (self, item):
    if self.root == None:
      self.root = Node (item)
    else:
      self.root = new_node_bst (self.root, item)

  def search_node (self, item):
    if self.root == None:
      return 'Бинарное дерево пусто'
    else:
      path = '\\' + search_node_bst (self.root, item)
    if '-1' in path:
      return 'Число не найдено'
    return path

  def delete_node (self, item):
    direction = self.search_node (item)
    if direction == 'Бинарное дерево пусто' or direction == 'Число не найдено':
      return direction
    self.root = func_del_node_bst (self.root, item)