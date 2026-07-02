class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_pair = [(p, s) for p, s in zip(position, speed)]
        pos_speed_pair.sort(reverse= True)
        stack = []
        for p, s in pos_speed_pair:
            if len(stack) == 0 or (target-p)/s > current_time:
                current_time = (target - p)/s 
                stack.append(current_time)
                continue
            else:
                continue
        return len(stack)
'''

7 4 1 0
1 2 2 1

distance = 10
Run TC1 :
         distance I create is the difference =


                    3  6  9  10 
now divide with speed to get time 
                    3  3  4.5  10  


Now We know that car cannot pass each other.

            ->   time 1 second :  8  6 3 1 
                      2 second :  9  8 5 2 
                      3 second :  10 10 7 3            
                      4 second :  -  -  9 4 
                      5 second :  -  -  10 5
                      .
                      .
                     10 second :  -  -  -  10 




'''
