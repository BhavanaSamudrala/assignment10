
from Node import Node


class Container(object):


    def __init__(self):
        self.__bottom = None
        self.__top = None
        self.__size = 0

    def size(self):
        """
        Purpose
            returns the number of data values in the stack
        Return:
            The number of data values in the stack
        """
        return self.__size

    def is_empty(self):
        """
        Purpose
            checks if the stack has no data in it
        Return:
            True if the stack has no data, or false otherwise
        """
        return self.__size == 0

    def add_top(self, value):
        """
        Purpose
             adds the given data value to the top
        Pre-conditions:
              value: data to be added
        Post-condition:
               the value is added to the top
        Return:
               (none)
        """
        self.__top = Node(value, self.__top)

        if self.__bottom is None:
            self.__bottom = self.__top

        self.__size += 1

    def add_bottom(self, value):
        """
        Purpose
             adds the given data value to the bottom
        Pre-conditions:
             value: data to be added
        Post-condition:
             the value is added
        Return:
              (none)
        """
        new_node = Node(value)

        if self.__size == 0:
            self.__top = new_node
        else:
            self.__bottom.set_next(new_node)

        self.__bottom = new_node
        self.__size += 1

    def pop_top(self):
        """
         Purpose
               Removes and returns a data value
               Note: it cannot be empty!
         Post-condition:
               the first value is removed
         Return:
               the first value or None
         """

        result = self.__top
        self.__top = self.__top.get_next()

        # check if it was last node.
        if self.__top is None:
            self.__bottom = None

        self.__size -= 1
        return result.get_data()

    def pop_bottom(self):
        """
         Purpose
              Removes and returns a data value
              Note: it cannot be empty!
         Post-condition:
               the last value is removed
         Return:
               the last value or None
         """

        if self.__size == 1:
            return self.pop_top()

        prev = self.__top
        current = prev.get_next()

        while current.get_next() is not None:
            prev = current
            current = current.get_next()

        prev.set_next(None)
        self.__bottom = prev
        self.__size -= 1
        return current.get_data()

    def peek(self):
        """
        Purpose
            returns the value from the top
            without removing it
            Note:  cannot be empty!
        Post-condition:
            None
        Return:
            the value at the top
        """
        return self.__top.get_data()

    def to_string(self):
        if self.is_empty():
            result = 'EMPTY'
        else:
            walker = self.__top

            value = walker.get_data()
            result = str(value) + ' |'

            while walker.get_next() is not None:
                walker = walker.get_next()

                value = walker.get_data()
                result += ' *-]-->[ ' + str(value) + ' |'

        return result
