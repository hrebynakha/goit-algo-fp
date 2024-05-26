"""
Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева,
необхідно створити програму на Python яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами,
використовуючи 16-систему RGB (приклад #1296F0).
Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу.
Кожен вузол при його відвідуванні має отримувати унікальний колір,
який візуально відображає порядок обходу.

"""
from collections import deque 

import networkx as nx
import matplotlib.pyplot as plt
from f_4 import build_tree, add_edges

def generate_color(iteration, ):
    """Generation color by iteration number"""
    #1296F0
    green = (iteration + 10) * 4 % 100
    blue = iteration * 2 % 10
    red = 12
    if green > 100:
        red = 2
    if green < 10:
        red = 14
    return f"#{red}{green}F{blue}"

def draw_colored_tree(tree_root):
    """Draw tree"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def dfs_search(tree, ):
    """DFS search visualition"""
    visited = set()
    stack = [tree]
    i = 0
    while stack:
        # Вилучаємо вершину зі стеку
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            node.color =  generate_color(i)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        else:
            print("Node visited", node.val)
        i += 1
        draw_colored_tree(tree)

def bfs_search(tree, ):
    """BFS search visualition"""
    visited = set()
    queue = deque([tree])
    i = 0
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            node.color =  generate_color(i)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        i += 1
        draw_colored_tree(tree)

if __name__ == "__main__":
    input_list = [11, 2, 5, 7, 100, 8, 10, 6, 13, 4, 99]
    tree = build_tree(input_list)
    dfs_search(tree)
    tree = build_tree(input_list)
    bfs_search(tree)
