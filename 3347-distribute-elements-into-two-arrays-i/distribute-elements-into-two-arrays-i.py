class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1=[nums[0]]
        a2=[nums[1]]
        for current_element in nums[2:]:
            if a1[-1]>a2[-1]:
                a1.append(current_element)
            else:
                a2.append(current_element)
        return a1+a2
        