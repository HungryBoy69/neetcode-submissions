class Solution:
    def isValid(self, s: str) -> bool:
        stack_array = []
        closeToOpen = {
              ')':'('
            , '}':'{'
            , ']':'['
            }
        for i in s:
            if i in closeToOpen:
                if stack_array and stack_array[-1] == closeToOpen[i]:
                    stack_array.pop()
                else:
                    return False
            else:
                stack_array.append(i)
        return True if not stack_array else False
             