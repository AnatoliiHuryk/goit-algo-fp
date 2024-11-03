class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 1. Функція реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 2. Функція сортування (злиттям) для однозв'язного списку
    def sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def sort(self):
        self.head = self.merge_sort(self.head)

    # 3. Функція об'єднання двох відсортованих однозв'язних списків
    def merge_with(self, other_list):
        self.head = self.sorted_merge(self.head, other_list.head)


list1 = LinkedList()
list1.append(4)
list1.append(2)
list1.append(1)
list1.append(3)

print("Початковий список 1:")
list1.print_list()

list1.reverse()
print("Список 1 після реверсування:")
list1.print_list()

list1.sort()
print("Список 1 після сортування:")
list1.print_list()

list2 = LinkedList()
list2.append(6)
list2.append(5)
list2.append(8)
list2.append(7)

print("Початковий список 2:")
list2.print_list()

list2.sort()
print("Список 2 після сортування:")
list2.print_list()

list1.merge_with(list2)
print("Об'єднаний відсортований список:")
list1.print_list()
