class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_array = [0] + flowerbed + [0]
        for i in range(1, len(new_array)-1):
            print('normal i ', i)
            if new_array[i+1] != 1 and new_array[i-1] != 1 and new_array[i] != 1 and n!=0:
                print('planted one')
                new_array[i] = 1
                n-=1
                print('after plant n =', n)
        return n == 0
