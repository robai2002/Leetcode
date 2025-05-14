class RandomizedSet:

    def __init__(self):
        self.hashTable = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        
        if val in self.hashTable:
            return False
        self.hashTable[val] = len(self.arr)
        self.arr.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.hashTable:
            return False
        self.hashTable[self.arr[-1]] = self.hashTable[val]
        self.arr[self.hashTable[val]] = self.arr[-1]
        self.arr.pop()
        self.hashTable.pop(val)
        return True


    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()