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

def left_exist (i, heap):
  if 2 * i < len (heap):
    return True
  else:
    return False
def right_exist (i, heap):
  if 2 * i + 1 < len (heap):
    return True
  else:
    return False

class Heap:
  def __init__ (self):
    self.items = [None,]
  
  def add (self, item):
    self.items.append (item)
    i = len (self.items) - 1
    while i > 1 and self.items [i] > self.items [i//2]:
      self.items [i], self.items [i//2] = self.items [i//2], self.items [i]
      i = i // 2
  
  def pop (self):
    if len (self.items) == 2:
      return self.items.pop ()
    res = self.items [1]
    self.items [1] = self.items.pop ()
    i = 1
    while right_exist (i, self.items) or left_exist (i, self.items):
      if left_exist (i, self.items) and not right_exist (i, self.items):
        if self.items [i] < self.items [2*i]:
          self.items [i], self.items [2*i] = self.items [2*i], self.items [i]
          i = 2 * i
        else:
          break
      elif not left_exist (i, self.items) and right_exist (i, self.items):
        if self.items [i] < self.items [2 * i + 1]:
          self.items [i], self.items [2*i+1] = self.items [2*i+1], self.items [i]
          i = 2 * i + 1
        else:
          break
      elif left_exist (i, self.items) and right_exist (i, self.items):
        if self.items [i] < self.items [2*i] and self.items [i] < self.items [2*i+1]:
          choice = max (self.items [2*i], self.items [2*i+1])
          if choice == self.items [2*i]:
            self.items [i], self.items [2*i] = self.items [2*i], self.items [i]
            i = 2 * i
          elif choice == self.items [2*i+1]:
            self.items [i], self.items [2*i+1] = self.items [2*i+1], self.items [i]
            i = 2 * i + 1
        elif self.items [i] < self.items [2*i]:
          self.items [i], self.items [2*i] = self.items [2*i], self.items [i]
          i = 2 * i
        elif self.items [i] < self.items [2*i+1]:
          self.items [i], self.items [2*i+1] = self.items [2*i+1], self.items [i]
          i = 2 * i + 1
        else:
          break
    return res

def heap_sort (lst):
  heap = Heap ()
  for item in lst:
    heap.add (item)
  for i in range (1, len (lst) + 1):
    lst [-i] = heap.pop ()
  return lst