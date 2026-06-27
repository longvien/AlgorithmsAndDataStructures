class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        nr = len(board)
        nc = len(board[0])
        directions = [[0, 1], [1, 0], [1, 1]]
        dp = [[(0, 0) for i in range(nc)] for k in range(nr)]
        dp[nr - 1][nc - 1] = (0, 1)
        for r in range(nr - 2, -1, -1):
            if r > -1:
                if board[r][nc - 1] != 'X':
                    dp[r][nc - 1] = (dp[r + 1][nc - 1][0] + int(board[r][nc - 1]), 1)
                else:
                    break
        for c in range(nc - 2, -1, -1):
            if c > -1:
                if board[nr - 1][c] != 'X':
                    dp[nr - 1][c] = (dp[nr - 1][c + 1][0] + int(board[nr - 1][c]), 1)
                else:
                    break
        for r in range(nr - 2, -1, -1):
            for c in range(nc - 2, -1, -1):
                if board[r][c] == 'X':
                    continue
                else:
                    curr = board[r][c]
                    if r == 0 and c == 0:
                        curr = 0
                    for dr, dc in directions:
                        oR = r + dr
                        oC = c + dc
                        if board[oR][oC] != 'X' and dp[oR][oC] != (0, 0):
                            if dp[r][c][0] < int(curr) + dp[oR][oC][0]:
                                dp[r][c] = (int(curr) + dp[oR][oC][0], dp[oR][oC][1])
                            elif dp[r][c][0] == int(curr) + dp[oR][oC][0]:
                                ways = (dp[r][c][1] + dp[oR][oC][1]) % 1000000007
                                dp[r][c] = (dp[r][c][0], ways)
        return [dp[0][0][0], dp[0][0][1]]