class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:

            if char == '(' or char == '{' or char == '[':
                stack.append(char)

            else:
                if not stack:
                    return False

                if stack[-1] == pair[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0