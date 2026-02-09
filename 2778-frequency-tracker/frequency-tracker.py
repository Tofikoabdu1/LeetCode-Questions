class FrequencyTracker:

    def __init__(self):
        self.d1 = defaultdict(int)
        self.d2 = defaultdict(int)
    def add(self, number: int) -> None:
        self.d2[self.d1[number]]-=1
        self.d1[number] += 1
        self.d2[self.d1[number]]+=1
    def deleteOne(self, number: int) -> None:
        self.d2[self.d1[number]] -= 1
        self.d1[number] = max(0,self.d1[number]-1)
        self.d2[self.d1[number]] +=1
    def hasFrequency(self, frequency: int) -> bool:
        return self.d2[frequency]>0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)