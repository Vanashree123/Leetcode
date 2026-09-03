class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1=set("qwertyuiop")
        r2=set("asdfghjkl")
        r3=set("zxcvbnm")
        result=[]
        for word in words:
            lower_word=set(word.lower())
            if lower_word <=r1 or lower_word <=r2 or lower_word <=r3:
                result.append(word)
        return result
        