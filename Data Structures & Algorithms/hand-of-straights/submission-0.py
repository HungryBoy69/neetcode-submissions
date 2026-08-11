from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        '''
            hand=[1,2,4,2,3,5,3,4]
            groupSize=4   1 = 1, 2 = 2 , 3 = 3 , 4 = 2 , 5 = 1
             1 2 2 3 3 4 4 5 if we have 1 then 1 2 3 4
        '''
        if len(hand)%groupSize!=0:
            return False
        countedArray = defaultdict(int)
        for num in hand:
            countedArray[num]+=1
        sortedCards = sorted(hand)
        for card in sortedCards:
            count = countedArray[card]
            if count == 0:
                continue
            for iter in range(card, card+groupSize):
                if countedArray[iter] < count:
                    return False                    
                countedArray[iter]-=1
        return True
        