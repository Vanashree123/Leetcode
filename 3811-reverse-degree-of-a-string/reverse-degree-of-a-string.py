class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        for i, char in enumerate(s, start=1):
            reversed_alphabet_idx = 26 - (ord(char) - ord('a'))
            total_sum += reversed_alphabet_idx * i
            
        return total_sum