class Solution:
    def calc_square(self, num):
        return num*num
    def isHappy(self, n: int) -> bool:
        visitedMap = {}
        str_num = str(n)
        visitedMap[str(n)] = 1
        if n == 1:
            return True
        while True:
            total_sum = 0
            for i in str_num:
                total_sum += self.calc_square(int(i))
            if str(total_sum) in visitedMap:
                return False
            if total_sum == 1:
                return True
            if str(total_sum) not in visitedMap:
                visitedMap[str(total_sum)] = 1
            str_num = str(total_sum)  