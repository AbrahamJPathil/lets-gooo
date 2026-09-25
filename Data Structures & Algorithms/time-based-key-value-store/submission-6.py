class TimeMap:

    def __init__(self):
        self.coll = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.coll[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        currColl = self.coll[key][::-1]
        l = 0
        r = len(currColl) - 1
        res = ""
        while(l <= r):
            mid = (l + r)//2
            if(currColl[mid][1] <= timestamp):
                    res = currColl[mid][0]
                    r = mid - 1
            else:
                l = mid + 1
        
        return res
        
