class Stack:
  def __init__ (self):
    self.items = []
  def push (self, item):
    self.items.append (item)
  def pop (self):
    if not self.isempty ():
      return self.items.pop ()
    else:
      return 'Стек пуст'
  def peek (self):
    return self.items [-1]
  def isempty (self):
    return len (self.items) == 0
