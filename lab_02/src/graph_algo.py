# Реализация графов
def generate_graph (n, lst_ribs):
  '''
  Генерирует матрицу смежности для графа и возвращает её.
  Параметры:
  - n (int) - количество вершин
  - lst_ribs (list) - список рёбер.
  Результат:
  - matrix_rel (list) - матрица смежности.
  '''
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
  '''
  Вспомогательная функция для relations_search.
  Конвертирует матрицу смежности в списки смежности.
  '''
  dict_graph = dict ()
  for i in range (len (matrix)):
    near_vor = set ()
    for j, item in enumerate (matrix [i]):
      if item == 1:
        near_vor.add (j)
    dict_graph [i] = near_vor
  return dict_graph

def relations_search (graph):
  '''
  Выполняет поиск компонента связности.
  Параметры:
  - graph (list) - матрица смежности графа.
  Результаты:
  - res (list) - список множеств, показывающих связность вершин.
  '''
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
  '''
  Вспомогательная функция для relations_search.
  Корректирует результат relations_search,
  увеличивая номера вершин на 1.
  (Начало нумерации смещается с 0 на 1.)
  '''
  res = []
  for item_a in graph:
    tmp = set ()
    for item_b in item_a:
      tmp.add (item_b + 1)
    res.append (tmp)
  return res
