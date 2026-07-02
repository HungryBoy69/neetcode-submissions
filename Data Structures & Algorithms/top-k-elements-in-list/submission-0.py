class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hash map to store the frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Create a heap to store the (frequency, number) pairs
        heap = []
        for num, count in freq.items():
            # Use a min-heap, but negate the frequency to simulate a max-heap
            heapq.heappush(heap, (-count, num))

        # Pop the top k elements from the heap
        result = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            result.append(num)

        return result
