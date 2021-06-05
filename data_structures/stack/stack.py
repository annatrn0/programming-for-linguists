#добавить параметр, который определяет max число элементов в стэке (если больше, то выводится ошибка)
"""
Programming for linguists

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """
    # pylint: disable=missing-module-docstring
    def __init__(self, max_num: int, data: Iterable = None):
        self.data = list(data) if data else []
        self.max_num = max_num

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        if len(self.data) >= self.max_num:
            return 'The stack is overflow!'
        else:
            self.data.append(element)
            return 'Element added!'

    def pop(self):
        """
        Delete the element on the top of stack
        """
        self.data.pop(-1)
        return 'Element deleted!'

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        return self.data[-1]

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return not bool(self.size())

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        return self.data[self.index]


# stack_1 = Stack(3, '2')
# print(stack_1.data)
# print(stack_1.push('1'))
# print(stack_1.data)
# print(stack_1.push('0'))
# print(stack_1.data)
# print(len(stack_1))
# print(iter(stack_1))
# print(next(stack_1))
# print(next(stack_1))
# print(stack_1.size())
# print(stack_1.push('2'))
# print(stack_1.data)
# print(stack_1.size())
