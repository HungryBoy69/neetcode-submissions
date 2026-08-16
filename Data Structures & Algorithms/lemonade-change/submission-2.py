from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_in = defaultdict(int)
        change = [10, 5]
        for bill in bills:
            if bill == 5:
                bill_in[bill]+=1
            else:
                balance = bill - 5
                for ch in change:
                    change_req = balance // ch
                    change_possible = min(change_req, bill_in[ch])
                    balance -=(ch * change_possible)
                    bill_in[ch]-=change_possible
                if balance > 0:
                    return False
                bill_in[bill]+=1
        return True