class BinaryTree:
    def __init__(self):
        """Инициализация пустого дерева"""
        self.root = None    # Корень дерева
    
    def insert(self, value):
        """Вставка нового значения в дерево"""
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Рекурсивная вспомогательная функция для вставки"""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Поиск значения в дереве"""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Рекурсивная вспомогательная функция для поиска"""
        if node is None or node.value == value:
            return node
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def inorder_traversal(self):
        """Обход дерева в порядке in-order"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Рекурсивная вспомогательная функция для in-order обхода"""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Обход дерева в порядке pre-order"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Рекурсивная вспомогательная функция для pre-order обхода"""
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """Обход дерева в порядке post-order"""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Рекурсивная вспомогательная функция для post-order обхода"""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)