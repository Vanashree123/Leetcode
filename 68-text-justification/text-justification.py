class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        cur_words = []
        cur_len = 0  

        for word in words:

            if cur_len + len(word) + len(cur_words) > maxWidth:
                total_spaces = maxWidth - cur_len
                
                if len(cur_words) == 1:
                    res.append(cur_words[0] + " " * total_spaces)
                else:
                    gaps = len(cur_words) - 1
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    
                    line = ""
                    for i in range(gaps):
                        spaces = space_per_gap + (1 if i < extra_spaces else 0)
                        line += cur_words[i] + " " * spaces
                    line += cur_words[-1] 
                    res.append(line)
            
                cur_words = []
                cur_len = 0

            cur_words.append(word)
            cur_len += len(word)

        last_line = " ".join(cur_words)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)

        return res