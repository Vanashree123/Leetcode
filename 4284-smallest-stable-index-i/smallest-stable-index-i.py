class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        min_suffix = [0] * n
        min_suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(nums[i], min_suffix[i + 1])
            
        current_max = nums[0]
        
        for i in range(n):
            current_max = max(current_max, nums[i])
            i_s = current_max - min_suffix[i]
            if i_s <= k:
                return i
                
        return -1