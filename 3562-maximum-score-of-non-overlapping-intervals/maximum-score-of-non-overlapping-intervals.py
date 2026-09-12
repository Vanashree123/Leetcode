from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store original index along with interval details
        # format: (l, r, weight, original_index)
        sorted_intervals = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        )
        
        # Sort by right boundary to enable standard interval DP
        sorted_intervals.sort(key=lambda x: x[1])
        
        # Extract right boundaries for binary search
        rights = [interval[1] for interval in sorted_intervals]
        
        # dp[c][i] = (max_score, list_of_indices) for taking up to c intervals from prefix i
        # Base state initialization
        dp = [[(0, ())] * (n + 1) for _ in range(5)]
        
        for i in range(1, n + 1):
            l, r, w, orig_idx = sorted_intervals[i - 1]
            
            # Find largest index j (1-based) where rights[j-1] < l
            j = bisect_right(rights, l - 1)
            
            for k in range(1, 5):
                # Option 1: Do not include current interval
                prev_score, prev_indices = dp[k][i - 1]
                best_score = prev_score
                best_indices = prev_indices
                
                # Option 2: Include current interval (if valid)
                take_score, take_indices = dp[k - 1][j]
                new_score = take_score + w
                new_indices = tuple(sorted(take_indices + (orig_idx,)))
                
                # Decision logic: Maximize weight; break ties lexicographically
                if new_score > best_score:
                    best_score = new_score
                    best_indices = new_indices
                elif new_score == best_score:
                    if best_indices == () or new_indices < best_indices:
                        best_indices = new_indices
                        
                dp[k][i] = (best_score, best_indices)
        
        return list(dp[4][n][1])