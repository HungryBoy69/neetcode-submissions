class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # while len(stones) > 1:
        #     stones.sort()
        #     cur = stones.pop() - stones.pop()
        #     if cur:
        #         stones.append(cur)
        # return stones[0] if stones else 0
        neg_stones = [-1*stone for stone in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            first = heapq.heappop(neg_stones)
            second = heapq.heappop(neg_stones)
            if second > first:
                heapq.heappush(neg_stones, first-second)
        '''
            Scenario 1 : there is only one stone remaining 
            Scenario 2: there were exactly two stones in the last iteration and both were equal so both got destroyed.
        '''
        neg_stones.append(0)  # either [0, -5] or could be [0]
        return abs(neg_stones[0])

            