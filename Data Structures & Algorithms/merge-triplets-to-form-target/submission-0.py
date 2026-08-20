class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        final_array = []
        for triplet in triplets:
            a, b, c = triplet
            if a == target[0] and b == target[1] and c == target[2]:
                return True
            if ( a <= target[0] and b <=target[1] and c <= target[2]):
                final_array.append(triplet)
        if not final_array:
            return False
        max_a, max_b, max_c = final_array[0][0], final_array[0][1], final_array[0][2]        
        for triplet in final_array:
            a, b, c = triplet
            max_a = max(a, max_a)
            max_b = max(b, max_b)
            max_c = max(c, max_c)
        
        if max_a == target[0] and max_b == target[1] and max_c == target[2]:
            return True

        return False
