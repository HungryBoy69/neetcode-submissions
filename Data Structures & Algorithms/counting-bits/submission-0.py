class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 1
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i #means i has reached a new power of 2 
            dp[i] = 1+dp[i-offset]
        return dp
'''
The key insight: the number of 1-bits in n equals 1 (for its highest set bit) 
plus the number of 1-bits in (n - offset), where offset is the largest power 
of 2 that is <= n. In other words, every number can be built by taking the 
largest power of 2 it contains and "adding" the bit pattern of whatever's left over.
We track that offset separately, and it only updates when i itself becomes 
the next power of 2.
i = 5, 6, 7:

offset starts at 1
i=1: 1==1*2? No wait — offset updates when i == offset*2. Let's trace properly:

i=1: offset*2=2, not equal to 1, so offset stays 1. dp[1] = 1 + dp[1-1] = 1 + dp[0] = 1. (binary: 1)
i=2: offset*2=2, equals i, so offset becomes 2. dp[2] = 1 + dp[2-2] = 1 + dp[0] = 1. (binary: 10)
i=3: offset*2=4, not equal to 3, offset stays 2. dp[3] = 1 + dp[3-2] = 1 + dp[1] = 2. (binary: 11)
i=4: offset*2=4, equals i, so offset becomes 4. dp[4] = 1 + dp[4-4] = 1 + dp[0] = 1. (binary: 100)
i=5: offset*2=8, not equal to 5, offset stays 4. dp[5] = 1 + dp[5-4] = 1 + dp[1] = 2. (binary: 101)
'''