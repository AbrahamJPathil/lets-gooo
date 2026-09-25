class TimeMap:

    def __init__(self):
        self.coll = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.coll[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        currColl = self.coll[key]
        for currVal in currColl[::-1]:
            if(currVal[1] <= timestamp):
                return currVal[0]
        
        return ""
