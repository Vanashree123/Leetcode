class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        indices = list(range(n))

        indices.sort(key=lambda index: -score[index])
      
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
      
        result = [""] * n
    
        for rank, athlete_index in enumerate(indices):
            if rank < 3:
               
                result[athlete_index] = medals[rank]
            else:
                result[athlete_index] = str(rank + 1)
      
        return result
