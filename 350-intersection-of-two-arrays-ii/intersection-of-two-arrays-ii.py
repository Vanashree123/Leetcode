class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fm=Counter(nums1)
        result=[]
        for num in nums2:
            if fm[num]>0:
                result.append(num)
                fm[num]-=1
        return result
