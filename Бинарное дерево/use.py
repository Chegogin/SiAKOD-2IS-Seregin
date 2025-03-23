# Пример использования
if __name__ == "__main__":
    tree = BinaryTree()
    
    # Вставляем значения
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        tree.insert(value)
    
    # Поиск
    print(f"Поиск 4: {tree.search(4) is not None}")  # True
    print(f"Поиск 9: {tree.search(9) is not None}")  # False
    
    # Разные обходы дерева
    print(f"In-order: {tree.inorder_traversal()}")    # [1, 3, 4, 5, 6, 7, 8]
    print(f"Pre-order: {tree.preorder_traversal()}")  # [5, 3, 1, 4, 7, 6, 8]
    print(f"Post-order: {tree.postorder_traversal()}")# [1, 4, 3, 6, 8, 7, 5]