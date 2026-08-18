from collections import Counter

class Solution:
    def findLHS(self, nums):
        freq = Counter(nums)

        result = 0

        for num in freq:
            if num + 1 in freq:
                length = freq[num] + freq[num + 1]
                result = max(result, length)

        return result