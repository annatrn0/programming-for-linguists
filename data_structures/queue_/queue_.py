#очередь с приоритетом - реализовать
"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    # pylint: disable=unused-argument,missing-module-docstring
    def __init__(self, priority: int, data: Iterable = (), max_size: int = None):
        self.priority = priority
        self.data = []
        for element in data:
            self.data.insert(priority, element) 

    def put(self, priority, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        self.priority = priority
        self.data.insert(self.priority, element)
        return 'Element put!'

    def get(self, priority):
        """
        Remove and return an item from queue_
        """
        self.priority = priority
        return self.data.pop(priority)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not self.data

    # pylint: disable=no-self-use
    def full(self) -> bool:
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if queue_ is not full
        """
        return False

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.data)

    def top(self):
        """
        Return the first element in queue_
        :return: Item from queue_
        """
        return self.data[-1]

    # pylint: disable=no-self-use
    def capacity(self) -> int:
        """
        Return the maximal size of queue_
        :return: Maximal size of queue_
        """
        return 0

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        return self.data[self.index]


# queue_1 = Queue_(1, '3')
# print(queue_1.data)
# print(queue_1.put(0, '1'))
# print(queue_1.data)
# print(queue_1.data[1])
# print(queue_1.get(1))
# print(queue_1.data)
