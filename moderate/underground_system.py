class UndergroundSystem:

    def __init__(self):
        self.checklist = defaultdict(list)
        self.trips = defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checklist[id].append((stationName, t))
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name, start = self.checklist[id].pop()
        self.trips[(name, stationName)][0] += (t - start)
        self.trips[(name, stationName)][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, trip = self.trips[(startStation, endStation)]
        
        return time / trip
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
