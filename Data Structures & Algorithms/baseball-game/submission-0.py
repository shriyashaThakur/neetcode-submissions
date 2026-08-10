class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = [] 
        total = 0

        for op in operations:

            if op == "+":
                new = stack[-1] + stack[-2]
                stack.append(new)
            
            elif op == "D":
                new = stack[-1] * 2
                stack.append(new)
            
            elif op == "C":
                stack.pop()

            else:
                stack.append(int(op))

        for score in stack:
            total += score 

        return total
