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

def relations_search (dict_graph):
  res = []
  way = {}
  for item in dict_graph.keys ():
    
