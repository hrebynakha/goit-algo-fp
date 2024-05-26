"""
Завдання 4. Візуалізація піраміди
Наступний код виконує побудову бінарних дерев.
Виконайте аналіз коду, щоб зрозуміти, як він працює.
Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.


"""
import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    def __str__(self, ):
        return str(self.val)

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def insert(root, key):
    if root is None:
        return Node(key)
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left is None:
            node.left = insert(node.left, key)
            break
        queue.append(node.left)
        if node.right is None:
            node.right = insert(node.right, key)
            break
        queue.append(node.right)
    return root


def build_tree(input_list):
    heapq.heapify(input_list)
    # Створення дерева
    root = Node(input_list[0])
    for el in input_list[1:]:
        root = insert(root, el)

    return root

input_list = [11, 2, 5, 7, 100, 8, 10, 6, 13, 4, 99]
tree = build_tree(input_list)
# Відображення дерева
draw_tree(tree)
