class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            M = {}
            M[0] = 0
            for i in range(1, amount + 1):
                M[i] = float('inf')
                for c in coins:
                    if i - c < 0: 
                        M[i - c] = float('inf')
                    else:
                        M[i] = min(
                            M[i],
                            M[i - c] + 1
                        )
                        
            if M[amount] == float('inf'): return -1
            return M[amount]