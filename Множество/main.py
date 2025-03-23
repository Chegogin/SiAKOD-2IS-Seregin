class MySet:
    def __init__(self, iterable=None):
        self.elements = {}
        if iterable is not None:
            for item in iterable:
                self.add(item)
    
    # Добавление элемента
    def add(self, item):
        self.elements[item] = None
    
    # Удаление элемента
    def remove(self, item):
        if item in self.elements:
            del self.elements[item]
        else:
            raise KeyError(f"Элемент {item} не найден в множестве")
    
    # Проверка наличия элемента
    def contains(self, item):
        return item in self.elements
    
    # Размер множества
    def size(self):
        return len(self.elements)
    
    # Проверка на пустоту
    def is_empty(self):
        return len(self.elements) == 0
    
    # Объединение множеств
    def union(self, other):
        result = MySet()
        for item in self.elements:
            result.add(item)
        for item in other.elements:
            result.add(item)
        return result
    
    # Пересечение множеств
    def intersection(self, other):
        result = MySet()
        for item in self.elements:
            if item in other.elements:
                result.add(item)
        return result
    
    # Разность множеств
    def difference(self, other):
        result = MySet()
        for item in self.elements:
            if item not in other.elements:
                result.add(item)
        return result
    
    # Проверка на подмножество
    def is_subset(self, other):
        for item in self.elements:
            if item not in other.elements:
                return False
        return True
    
    # Очистка множества
    def clear(self):
        self.elements.clear()
    
    # Преобразование в список
    def to_list(self):
        return list(self.elements.keys())
    
    # Строковое представление
    def __str__(self):
        return "{" + ", ".join(str(key) for key in self.elements.keys()) + "}"

# Пример использования
if __name__ == "__main__":
    # Создание множеств
    set1 = MySet([1, 2, 3, 4])
    set2 = MySet([3, 4, 5, 6])
    
    # Добавление элемента
    set1.add(5)
    print("Set1:", set1)  # {1, 2, 3, 4, 5}
    
    # Проверка наличия
    print("Содержит 3:", set1.contains(3))  # True
    print("Содержит 7:", set1.contains(7))  # False
    
    # Удаление элемента
    set1.remove(2)
    print("После удаления 2:", set1)  # {1, 3, 4, 5}
    
    # Операции с множествами
    print("Объединение:", set1.union(set2))          # {1, 3, 4, 5, 6}
    print("Пересечение:", set1.intersection(set2))  # {3, 4, 5}
    print("Разность:", set1.difference(set2))       # {1}
    
    # Размер и проверка на пустоту
    print("Размер set1:", set1.size())  # 4
    print("Пустое ли:", set1.is_empty())  # False
    
    # Проверка на подмножество
    set3 = MySet([3, 4])
    print("set3 - подмножество set1:", set3.is_subset(set1))  # True
    
    # Очистка
    set3.clear()
    print("Очищенное set3:", set3)  # {}