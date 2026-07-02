class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans_wo_zero = 1
        flag = 0
        count = 0 
        ans = []
        for i in nums:
            if i == 0:
                count+=1
                flag = 1
                continue 
            else:
                ans_wo_zero = ans_wo_zero * i
        
        for i in nums:
            if flag == 1:  # the product is zero . So except zero there will be product alsways zero
                if i == 0:
                    if count > 1:
                        ans.append(0)
                    else:
                        ans.append(ans_wo_zero)
                else:
                    ans.append(0)
            else:
                ans.append(int(ans_wo_zero/i))
        return ans 