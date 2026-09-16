class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [n+1 for n in range(n)]
        ans = []
        def traverse(idx, current):
            if idx >= n:
                if len(current) == k:
                    ans.append(current.copy())
                return 
            current.append(arr[idx])
            traverse(idx+1, current)
            current.pop()
            traverse(idx+1, current)
        traverse(0, [])
        return ans