from a10provided.a10q2_Container import Container


class Stack(Container):

    def __init__(self):
        """
        Purpose
             creates an empty stack
        """
        Container.__init__(self)

    def pop(self):
        """
        Purpose
             Removes and returns a data value from the stack.
             Note: the stack cannot be empty!
        Post-condition:
             the first value is removed from the stack
        Return:
             the first value in the stack, or None
        """
        return Container.pop_top(self)

    def push(self, value):
        """
        Purpose
            adds the given data value to the stack
        Pre-conditions:
             value: data to be added
        Post-condition:
            the value is added to the stack
        Return:
            (none)
        """
        Container.add_top(self, value)

    def peek(self):
        """
        Purpose
            returns the value from the top of given stack
             without removing it
             Note: the stack cannot be empty!
        Post-condition:
              None
        Return:
             the value at the top of the stack
        """
        return Container.peek(self)
