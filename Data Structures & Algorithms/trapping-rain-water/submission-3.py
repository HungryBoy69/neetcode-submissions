class Solution:
    def trap(self, height: List[int]) -> int:
        max_num = 0
        left_max, right_max = [], []
        for i in range(1,len(height)):
            max_num = max(max_num, height[i-1])
            left_max.append(max_num)
        print('check', left_max)
        max_sum = 0
        for i in range(len(height)-1, -1, -1):
            print(i)
            if i == len(height) -1 :
                right_max.append(0)
                continue
            max_sum = max(max_sum, height[i+1])
            right_max.append(max_sum)
        print('check right', right_max)
        ans = 0
        for i in range(1, len(height)-1):
            print(i)
            res = min(left_max[i], right_max[len(height)-i])- height[i]
            if res > 0:
                ans +=res
        return ans

                
                
            