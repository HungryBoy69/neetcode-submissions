class TimeMap:

    def __init__(self):
        self.hash_keys  = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_keys:
            self.hash_keys[key] = []
        self.hash_keys[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_keys:
            return ""
        values = self.hash_keys.get(key, [])
        l , r = 0 , len(values) - 1
        res = ""
        while l <= r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m+1
            else:
                r = m -1 
        return res 
