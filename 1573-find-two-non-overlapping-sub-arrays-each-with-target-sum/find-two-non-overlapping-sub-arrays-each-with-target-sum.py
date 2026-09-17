class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        
        left = 0
        curr_sum = 0
        ans = float('inf')
        best_till_now = float('inf')
        
        for right in range(n):
            curr_sum += arr[right]
         
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == target:
                current_len = right - left + 1
                
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, current_len + min_len[left - 1])
                
                best_till_now = min(best_till_now, current_len)
            
            min_len[right] = best_till_now
        
        return ans if ans != float('inf') else -1