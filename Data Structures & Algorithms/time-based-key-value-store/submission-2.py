class TimeMap:

    def __init__(self):
        self.mapValues = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapValues: 
            self.mapValues[key] = {}
        if timestamp not in self.mapValues[key]: 
            self.mapValues[key][timestamp] = []
        self.mapValues[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.mapValues: 
            return ""
        seen = 0

        for time in self.mapValues[key]: 
            if time <= timestamp: 
                seen = max(seen, time)

        return "" if seen == 0 else self.mapValues[key][seen][-1]