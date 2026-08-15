class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operator = {'+', '-', '*', '/' }
        val = []
        for t in tokens:
            if t not in operator:
                val.append(int(t))
            else:
                right = val.pop()
                left = val.pop()

                if t == "+":
                    new = left + right 
                    val.append(new)
                elif t == "-":
                    new = left - right
                    val.append(new)
                elif t == "*":
                    new = left * right
                    val.append(new)
                elif t == "/":
                    new = int(left / right)
                    val.append(new)

        return val[-1]

                                
