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
