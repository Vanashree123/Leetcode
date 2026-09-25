class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        stack = [[]]

        def concatenate(set1: set, set2: set) -> set:
            return {s1 + s2 for s1 in set1 for s2 in set2}

        i = 0
        n = len(expression)

        while i < n:
            char = expression[i]

            if char.isalpha():
          
                j = i
                while j < n and expression[j].isalpha():
                    j += 1
                word = expression[i:j]
                
                if stack and stack[-1] and stack[-1][-1] != ',':
                    prev = stack[-1].pop()
                    stack[-1].append(concatenate(prev, {word}))
                else:
                    stack[-1].append({word})
                i = j - 1

            elif char == '{':
           
                stack.append([])

            elif char == ',':
                stack[-1].append(',')

            elif char == '}':
                curr_group = stack.pop()
                res = set()
                for item in curr_group:
                    if item != ',':
                        res.update(item)

            
                if stack and stack[-1] and stack[-1][-1] != ',':
                    prev = stack[-1].pop()
                    stack[-1].append(concatenate(prev, res))
                else:
                    stack[-1].append(res)

            i += 1

   
        final_set = set()
        for item in stack[0]:
            if item != ',':
                final_set.update(item)

        return sorted(list(final_set))