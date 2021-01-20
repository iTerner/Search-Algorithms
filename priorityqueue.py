class PriorityQueue:
    def __init__(self, f):
        self.elements = []  # list of all the elements
        self.f = f  # the function for our queue
        self.count_of_elements = 0  # the count of elements

    """
    The function returns True if the queue is empty, otherwise False 
    """

    def is_empty(self):
        return self.count_of_items == 0

    """
    The function add the node to the queue
    """

    def add(self, node):
        self.elements.append(node)
        self.count_of_elements += 1

    """
    The function removes the node with the lowest f-value from the queues
    """

    def remove(self):
        min_val = float("inf")
        min_index = 0
        counter = 0
        for e in self.elements:
            v = self.f(e)
            if v < min_val:
                min_val = v
                min_index = counter
            counter += 1
        node = self.elements[min_index]
        del self.elements[min_index]
        self.count_of_elements -= 1
        return node

    """
    The function remove a specific node from the queue
    """

    def remove(self, node):
        counter = 0
        for e in self.elements:
            if e.compare(node):
                del self.elements[counter]
            counter += 1

    """
    The function checks if the node is inside the queue
    """

    def is_in_queue(self, node):
        for e in self.elements:
            if e.compare(node):
                return True
        return False

    """
    The function gets a node that is in the queue and returns his f-cost value
    """

    def get_value(self, node):
        for e in self.elements:
            if e.compare(node):
                return f(e)
        return False
