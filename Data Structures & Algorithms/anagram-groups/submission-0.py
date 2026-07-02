class Solution:
    def groupAnagrams(self, nums: List[str]) -> List[List[str]]:
        ans_list =  []
        done_index = []
        for i in range(0, len(nums)-1):
            print(i, ',', nums[i])
            if i not in done_index:
                print('not in done index list')
                first = ''.join(sorted(nums[i]))
                print(first,'the first is')
                done_index.append(i)
                print(done_index, 'after pushing in list')
            else:
                print('continuing since already considered')
                continue
            sub_list = []
            for j in range(i+1, len(nums)):
                print(j, ',' , 'the iteration is', nums[j])
                second = ''.join(sorted(nums[j]))
                print(second, 'the second is')
                print(first == second)
                if first == second and j not in ans_list:
                    sub_list.append(nums[j])
                    done_index.append(j)
            sub_list.append(nums[i])
            print(sub_list)
            ans_list.append(sub_list)
            print(ans_list)
            print(done_index, 'the done index is')
        print(done_index, len(nums)-1)
        print(nums[len(nums)-1])
        if len(nums)-1 not in done_index:
            ans_list.append([nums[len(nums)-1]])
           
        return ans_list
            