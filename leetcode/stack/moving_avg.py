# Author: Gaurav Pande
## Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
class MovingAverage(object):
    def __init__(self, size):
        self.size = size
        self.queue = []

    def next(self, val):
        if not self.queue or len(self.queue) < self.size:
            self.queue.append(val)
        else:
            self.queue.pop(0)
            self.queue.append(val)
        return float(sum(self.queue)) / len(self.queue)