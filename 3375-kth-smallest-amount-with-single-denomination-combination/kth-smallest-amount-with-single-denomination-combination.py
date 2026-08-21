import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        

        subsets = []
        for mask in range(1, 1 << n):
            lcm_val = 1
            count = 0
            for i in range(n):
                if (mask >> i) & 1:
                    lcm_val = math.lcm(lcm_val, coins[i])
                    count += 1
          
            sign = 1 if count % 2 == 1 else -1
            subsets.append((lcm_val, sign))
            
        def count_multiples(m: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (m // lcm_val)
            return total

 
        left = 1
        right = min(coins) * k
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count_multiples(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans