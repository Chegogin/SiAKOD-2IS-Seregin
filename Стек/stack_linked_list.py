from node import Node

class StackLinkedList:
    def __init__(self):
        """Инициализация пустого стека"""
        self.top = None
        self._size = 0
    
    def push(self, item):
        """Добавление элемента в вершину стека"""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    
    def pop(self):
        """Удаление и возврат элемента с вершины стека"""
        if self.is_empty():
            raise IndexError("Стек пуст")
        popped_item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_item
    
    def peek(self):
        """Просмотр элемента на вершине стека без удаления"""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.top.data
    
    def is_empty(self):
        """Проверка, пуст ли стек"""
        return self.top is None
    
    def size(self):
        """Возврат размера стека"""
        return self._size
    
    def __str__(self):
        """Строковое представление стека"""
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + " -> ".join(items) + "]"