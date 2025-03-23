class StackList:
    def __init__(self):
        """Инициализация пустого стека"""
        self.items = []
    
    def push(self, item):
        """Добавление элемента в вершину стека"""
        self.items.append(item)
    
    def pop(self):
        """Удаление и возврат элемента с вершины стека"""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()
    
    def peek(self):
        """Просмотр элемента на вершине стека без удаления"""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items[-1]
    
    def is_empty(self):
        """Проверка, пуст ли стек"""
        return len(self.items) == 0
    
    def size(self):
        """Возврат размера стека"""
        return len(self.items)
    
    def __str__(self):
        """Строковое представление стека"""
        return str(self.items)