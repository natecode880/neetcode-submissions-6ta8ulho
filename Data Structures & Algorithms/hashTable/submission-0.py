class Pair:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.value = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = [None] * self.capacity
    
    def hash(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        start_index = index
        while True:
            if self.map[index] is None:
                self.map[index] = Pair(key,value)
                self.size += 1
                if self.size / self.capacity >= 0.5:
                    self.resize()
                return
            elif self.map[index].key == key:
                self.map[index].value = value
                return

            index = (index + 1) % self.capacity

            if index == start_index:
                self.resize()
                self.insert(key, value)
                return

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        start_index = index
        while True:
            if self.map[index] == None:
                return False
            elif self.map[index].key == key:
                self.map[index] = None
                # Rehash to handle the 'gap' created by deletion in open addressing
                self.size -= 1
                next_index = (index + 1) % self.capacity
                while self.map[next_index] is not None:
                    temp = self.map[next_index]
                    self.map[next_index] = None
                    self.size -= 1
                    self.insert(temp.key, temp.value)
                    next_index = (next_index + 1) % self.capacity
                return True

            index = (index + 1) % self.capacity

            if index == start_index:
                return False

    def get(self, key: int) -> int:
        index = self.hash(key)
        start_index = index
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].value
            index = (index + 1) % self.capacity

            if index == start_index:
                break

        return -1

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_map = self.map
        self.capacity = self.capacity * 2
        self.size = 0
        self.map = [None] * self.capacity
        for item in old_map:
            if item:
                self.insert(item.key, item.value)