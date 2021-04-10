from a10provided.a10q2_Container import Container


class Queue(Container):

    def __init__(self):
        """
        Purpose
             creates an empty queue
        """
        Container.__init__(self)

    def dequeue(self):
        """
        Purpose
             removes and returns a data value from the queue
             Note: the queue cannot be empty!
        Post-condition:
             the first value is removed from the queue
        Return:
             the first value in the queue, or None
        """
        return Container.pop_top(self)
    def enqueue(self,value):
        """
        Purpose
              adds the given data value to the queue
        Pre-conditions:
              value: data to be added
        Post-condition:
             the value is added to the queue
        Return:
             (none)
        """
        return Container.add_bottom(self,value)

    def peek(self):
        """
        Purpose
             returns the value from the top without removing it
             Note: the queue cannot be empty!
        Post-condition:
              None
        Return:
              the value at the top of the queue
        """
        return Container.peek(self)