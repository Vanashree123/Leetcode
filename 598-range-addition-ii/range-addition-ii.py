class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row_limit=m
        min_col_limit=n

        for row_limit,col_limit in ops:
            min_row_limit=min(min_row_limit,row_limit)
            min_col_limit=min(min_col_limit,col_limit)
        return min_row_limit * min_col_limit

        