class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ["[", "(", "{"]:
                stack.append(char)
            elif char in ["]", ")", "}"]:
                # Stupid edge case of ']'
                if len(stack) == 0:
                    return False


                last_char = stack[len(stack) - 1]
                translate = {"[": "]", "{": "}", "(": ")"}

                if translate[last_char] == char:
                    stack.pop()
                else:
                    return False

        if len(stack) > 0:
            return False
        return True
