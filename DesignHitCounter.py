import collections

class HitCounter:

    def __init__(self):
        self.deque = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.deque.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # pop left all timestamps older than 5 minutes
        while self.deque and (timestamp - self.deque >= 300):
            self.deque.popleft()
        # the len of the rest timestamps is the answer
        return len(self.deque)

