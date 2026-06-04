class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=self.sortEnd)
        total = 1
        current = 0
        currentNext = 1
        while currentNext < len(pairs):
            if pairs[current][1] < pairs[currentNext][0]:
                total += 1
                current = currentNext
                currentNext +=1
            else:
                currentNext += 1
        return total
    def sortEnd(self, pair):
        return pair[1]