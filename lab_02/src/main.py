# Выполнил: Ставецкий Максим Иванович
# Вариант 24
'''
Граф. Вершины и Ребра
8 верш: (1,2), (2,3), (3,4), (4,5),
(5,6), (6,7), (7,8)
Дерево. Элементы для построения
{35, 26, 42, 24, 28, 37, 45}
Дерево. Найти / Удалить
Найти: 42,
Уд.: 26
Куча. Массив для Heap Sort
[35, 26, 42, 24, 28, 37, 45]
'''
from graph_algo import *
from tree_algo import *

n = 8
lst_ribs = [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8)]
matrix_rel = generate_graph (n, lst_ribs)
print ('Матрица смежности')
for item in matrix_rel:
  print (item)
print ('Поиск компонента связности')
res_search = relations_search (matrix_rel)
print (correct_print_search (res_search))

tree = BST ()
for item in [35, 26, 42, 24, 28, 37, 45]:
  tree.new_node (item)
print ('Дерево')
print ('Поиск элемента', 42)
print (tree.search_node (42))
tree.delete_node (26)
print ('Поиск удалённого элемента', 26)
print (tree.search_node (26))