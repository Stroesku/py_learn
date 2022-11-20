class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        #Ограничитель
        self.top = Node()

    def append(self, value):
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        current.next_node = Node(value)

    def __str__(self):
        current = self.top.next_node
        values = "["
        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node
        return values + "]"


list = LinkedList()
list.append(23)
list.append(45)
list.append(88)
list.append(34)
list.append(22)

print(list)