class Solution:

    def smaller_on_left(self, heights):
        stack = []
        smaller_left = []
        for i in range(0, len(heights)):
            if len(stack) == 0:
                stack.append((heights[i], i))
                smaller_left.append(-1)
            else:
                while len(stack) >0:
                    if heights[i] <= stack[-1][0]:
                        stack.pop()
                        if len(stack)==0:
                            smaller_left.append(-1)
                            break
                    else:
                        smaller_left.append(stack[-1][1])
                        stack.append((heights[i], i))
                        break
                stack.append((heights[i], i))
        return smaller_left
    def smaller_on_right(self, heights):
        stack = []
        smallest_right = []
        for i in range(len(heights)-1, -1, -1):
            if len(stack)==0:
                stack.append((heights[i], i))
                smallest_right.append(-1)
            else:
                while len(stack)>0:
                    if heights[i] <= stack[-1][0]:
                        stack.pop()
                        if len(stack)==0:
                            smallest_right.append(-1)
                            break
                    else:
                        smallest_right.append(stack[-1][1])
                        stack.append((heights[i], i))
                        break
                stack.append((heights[i], i))
        return smallest_right[::-1]

    def largestRectangleArea(self, heights: List[int]) -> int:
        left = self.smaller_on_left(heights)
        right = self.smaller_on_right(heights)
        area = -1
        print(left)
        print(right)
        for i in range(0, len(heights)):
            left_range = -1 if left[i] == -1  else left[i]
            right_range = len(heights) if right[i] == -1 else right[i]
            print(left_range, right_range)
            width = right_range - left_range -1
            # print('areas is ',area, width* heights[i]) 
            area = max(width* heights[i],area)
        return area