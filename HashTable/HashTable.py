class hashTable:
    def __init__(self):
        self.table = [[] for i in range(10)] # create 10 arrays in big array

    def hashCode(self, key) -> int:
        result = 0
        for i in key:
            result = result * 7 + ord(i)
        return result

    def index(self, key):
        return self.hashCode(key) % len(self.table)

    def set(self, key, value):
        index = self.index(key)
        i = 0
        while i < len(self.table[index]):
            if self.table[index][i][0] == key:
                self.table[index][i] = (key, value)
                return
            i+=1
        self.table[index].append((key, value))

    def get(self, key):
        index = self.index(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.index(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].remove((k, v)) # or del list[i]
        return None