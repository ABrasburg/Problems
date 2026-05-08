# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish
# this with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

class Log(): # O(n) time complexity y O(n) space complexity
    def __init__(self, n):
        self.log = []
        self.n = n

    def record(self, order_id):  #O(n)
        if len(self.log) == self.n:
            self.log.pop(0) # O(n) time complexity
        self.log.append(order_id) # O(1) time complexity

    def get_last(self, i): # O(1)
        if i > len(self.log):
            return None
        return self.log[-i]
    
class Log_mejorado(): # O(1) time complexity y O(m) space complexity
    # Donde m es el total de logs guardados
    def __init__(self, n):
        self.log = []
        self.n = n
        self.index = 0

    def record(self, order_id):  #O(1)
        if len(self.log) < self.n:
            self.log.append(order_id)
        else:
            self.log[self.index] = order_id
        self.index = (self.index + 1) % self.n

    def get_last(self, i): # O(1)
        if i > len(self.log):
            return None
        return self.log[-i]