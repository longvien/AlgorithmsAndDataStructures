class Solution:
    def maximum69Number(self, num: int) -> int:
        n = str(num)
        for i in range(len(n)):
            if n[i] == '6':
                n = n[:i] + '9' + n[i + 1:]
                break
        return int(n)
mySolu = Solution()
print(mySolu.maximum69Number('9669'))