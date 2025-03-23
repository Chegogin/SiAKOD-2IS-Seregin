class CircularQueue:
    def __init__(self, capacity):
        """Инициализация очереди с заданной емкостью"""
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0  # Указатель на начало
        self.rear = -1  # Указатель на конец
        self.count = 0  # Текущее количество элементов
    
    def is_empty(self):
        """Проверка на пустоту"""
        return self.count == 0
    
    def is_full(self):
        """Проверка на заполненность"""
        return self.count == self.capacity
    
    def enqueue(self, item):
        """Добавление элемента"""
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = item
            self.count += 1
        else:
            raise IndexError("Очередь переполнена")
    
    def dequeue(self):
        """Удаление и возврат элемента"""
        if not self.is_empty():
            item = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.count -= 1
            return item
        raise IndexError("Очередь пуста")
    
    def peek(self):
        """Просмотр первого элемента"""
        if not self.is_empty():
            return self.items[self.front]
        raise IndexError("Очередь пуста")
    
    def size(self):
        """Возврат текущего размера"""
        return self.count

# Пример использования
if __name__ == "__main__":
    queue = CircularQueue(3)
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print(f"Размер: {queue.size()}")  # 3
    print(f"Первый элемент: {queue.peek()}")  # 1
    
    print(f"Извлечено: {queue.dequeue()}")  # 1
    print(f"Размер: {queue.size()}")  # 2
    
    queue.enqueue(4)  # Добавляем в освободившееся место
    print(f"Размер: {queue.size()}")  # 3