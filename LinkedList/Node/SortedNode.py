class sortedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
    def __lt__(self, value) -> int:
        return self.value - value