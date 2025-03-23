class Node:
    def __init__(self, data):
        self.data = data  # Значение узла
        self.next = None  # Ссылка на следующий узел

class LinkedList:
    def __init__(self):
        self.head = None  # Начало списка
    
    # Добавление элемента в конец списка
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    # Добавление элемента в начало списка
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Удаление элемента по значению
    def delete(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next
    
    # Поиск элемента
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    # Получение длины списка
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    # Вывод списка
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    # Вставка по индексу
    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise IndexError("Индекс вне диапазона")
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

# Пример использования
if __name__ == "__main__":
    # Создаем список
    llist = LinkedList()
    
    # Добавляем элементы
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.prepend(0)
    
    # Выводим список
    print("Список:", llist.display())  # [0, 1, 2, 3]
    
    # Проверяем поиск
    print("Есть 2:", llist.search(2))  # True
    print("Есть 5:", llist.search(5))  # False
    
    # Вставка по индексу
    llist.insert_at(2, 10)
    print("После вставки:", llist.display())  # [0, 1, 10, 2, 3]
    
    # Удаление элемента
    llist.delete(10)
    print("После удаления:", llist.display())  # [0, 1, 2, 3]
    
    # Длина списка
    print("Длина:", llist.length())  # 4