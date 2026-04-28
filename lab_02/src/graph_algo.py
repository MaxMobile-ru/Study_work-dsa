# Реализация графов
from collections import deque
def generate_graph (n, lst_ribs):
  matrix_rel = []
  for _ in range (n):
    tmp = []
    for _ in range (n):
      tmp.append (0)
    matrix_rel.append (tmp)
  for item in lst_ribs:
    start = item [0]
    end = item [1]
    matrix_rel [start - 1] [end - 1] = 1
    matrix_rel [end - 1] [start - 1] = 1
  return matrix_rel

def matrix_to_dict (matrix):
  dict_graph = dict ()
  for i in range (len (matrix)):
    near_vor = set ()
    for j, item in enumerate (matrix [i]):
      if item == 1:
        near_vor.add (j)
    dict_graph [i] = near_vor
  return dict_graph

def relations_search (graph):
  graph = matrix_to_dict (graph)
  res = []
  queue = []
  is_visited_lst = []
  for _ in range (len (graph.keys ())):
    is_visited_lst.append (False)
  current = 0
  while False in is_visited_lst:
    if len (queue) == 0:
      is_visited_lst [current] = True
      queue.append (current)
    else:
      current += 1
    queue_now = queue [current]
    for item in graph [queue_now]:
      if not (item in set (queue)):
        is_visited_lst [item] = True
        queue.append (item)
        if not (False in is_visited_lst):
          res.append (set (queue))
  return res
