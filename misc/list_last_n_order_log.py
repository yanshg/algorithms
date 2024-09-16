'''
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

Implementing a circular buffer suffices the requirement. It takes O(1) to record and get last ith. 

'''

class OrderLog:
    def __init__(self, n):
        self.capacity = n
        self.order_ids = [ None ] * n
        self.curr_index = 0

    def record(self, order_id):
        self.order_ids[self.curr_index] = order_id
        self.curr_index = (self.curr_index + 1) % self.capacity

    def get_last(self, i):
        index = (self.curr_index - i + self.capacity) % self.capacity
        return self.order_ids[index]

N = 3    
orderlog = OrderLog(N)
orderlog.record(1)
orderlog.record(2)
orderlog.record(3)

assert orderlog.get_last(1) == 3
