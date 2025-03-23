from stack_list import StackList
from stack_linked_list import StackLinkedList

def test_stack_list():
    stack_list = StackList()
    print("StackList:")
    print("Пустой ли стек?", stack_list.is_empty())
    stack_list.push(1)
    stack_list.push(2)
    stack_list.push(3)
    print("После добавления элементов:", stack_list)
    print("Размер:", stack_list.size())
    print("Верхний элемент:", stack_list.peek())
    print("Извлечённый элемент:", stack_list.pop())
    print("После извлечения:", stack_list)

def test_stack_linked_list():
    stack_linked = StackLinkedList()
    print("\nStackLinkedList:")
    print("Пустой ли стек?", stack_linked.is_empty())
    stack_linked.push("a")
    stack_linked.push("b")
    stack_linked.push("c")
    print("После добавления элементов:", stack_linked)
    print("Размер:", stack_linked.size())
    print("Верхний элемент:", stack_linked.peek())
    print("Извлечённый элемент:", stack_linked.pop())
    print("После извлечения:", stack_linked)

if __name__ == "__main__":
    test_stack_list()
    test_stack_linked_list()