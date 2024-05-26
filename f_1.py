"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
            if cur is None:
                return
            prev.next = cur.next
            cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print()
    def reverse(self, ):
        # 1 > 2 > 3 ==>> 3 > 2 > 1
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        # update head for last prev node
        self.head = prev

    def get_middle(self, head):
        """Get mid element"""
        if head is None:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, left, right):
        """ Sorting by merge alg"""
        if left is None:
            return right
        if right is None:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result

    def merge_sort(self, head):
        """ Merge sort duncfion"""
        if head is None or head.next is None:
            return head
        middle = self.get_middle(head)
        middle_next = middle.next
        middle.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(middle_next)
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def sort(self, ):
        """Sort function """
        # change head of linked list to sorted merged list
        self.head = self.merge_sort(self.head)

    def merge(self, sorted_linked_list):
        """Merge list with second sorted list"""
        node = Node()
        head = node
        head1 = self.head
        head2 = sorted_linked_list.head
        while head1 and head2:
            if head1.data <= head2.data:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next

        if head1:
            head.next = head1
        elif head2:
            head.next = head2

llist = LinkedList()
# append elements
llist.insert_at_beginning(5)
llist.insert_at_beginning(1)
llist.insert_at_beginning(15)


print("Linked list:")

llist.print_list()
print("Reversed list:")
llist.reverse()
llist.print_list()

print("Sorted list:")
llist.sort()
llist.print_list()


second_list = LinkedList()
second_list.insert_at_beginning(10)
second_list.insert_at_beginning(18)
second_list.insert_at_beginning(4)
print("Linked list 2:")
second_list.print_list()
print("Sorted sercond list:")
second_list.sort()
second_list.print_list()

llist.merge(second_list)
print("Merged with sercond list:")
llist.print_list()
