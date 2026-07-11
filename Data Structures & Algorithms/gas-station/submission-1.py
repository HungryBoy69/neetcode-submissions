class Solution:
      def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start, end = 0, 0
        tank = gas[0]
        visited = 0  # how many stations we've pulled into the window

        while visited < n:
            if tank >= cost[end]:
                # can move end forward
                tank -= cost[end]
                end = (end + 1) % n
                tank += gas[end]
            else:
                # end is stuck, try to pull start back
                start = (start - 1) % n
                if start == end:
                    return -1  # wrapped all the way around, no room left to pull back we might have 
                    #covered all stations but still we hit the else loop meaning we did not have enough fuel to touch all the elements in the array
                tank += gas[start] - cost[start]

            visited += 1

        return start if start == end else -1