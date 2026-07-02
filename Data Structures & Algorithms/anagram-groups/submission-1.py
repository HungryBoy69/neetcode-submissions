class Solution:
    def groupAnagrams(self, nums: List[str]) -> List[List[str]]:
        ans_list, done_index = [], []
        for i in range(0, len(nums)-1):
            if i not in done_index:
                first = ''.join(sorted(nums[i]))
                done_index.append(i)
            else:
                continue
            sub_list = []
            for j in range(i+1, len(nums)):
                second = ''.join(sorted(nums[j]))         
                if first == second and j not in ans_list:
                    sub_list.append(nums[j])
                    done_index.append(j)
            sub_list.append(nums[i])
            ans_list.append(sub_list)

        if len(nums)-1 not in done_index:
            ans_list.append([nums[len(nums)-1]])
           
        return ans_list
            