# Реализация графов
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
  i = 0
  current = 0
  while False in is_visited_lst:
    if len (queue) == 0:
      is_visited_lst [current] = True
      queue.append (current)
    else:
      i += 1
      if i == len (queue):
        res.append (set (queue))
        current = is_visited_lst.index (False)
        i = 0
        queue = []
        continue
    current = queue [i]
    for item in graph [current]:
      if not (item in set (queue)):
        is_visited_lst [item] = True
        queue.append (item)
        if not (False in is_visited_lst):
          res.append (set (queue))
    if len (graph [current]) == 0:
      res.append (set (queue))
      if False in is_visited_lst:
        current = is_visited_lst.index (False)
        i = 0
        queue = []
  return res

def correct_print_search (graph):
  res = []
  for item_a in graph:
    tmp = set ()
    for item_b in item_a:
      tmp.add (item_b + 1)
    res.append (tmp)
  return res
