class TimeMap:

    def __init__(self):
        self.coll = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.coll[key] = [value,timestamp]

    def get(self, key: str, timestamp: int) -> str:
        currVal = self.coll[key]
        if(currVal[1] <= timestamp):
            return currVal[0]
        else:
            return ""
