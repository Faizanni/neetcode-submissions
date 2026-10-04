class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num_elements = 0
        self.dynarray = [None] * capacity

    def get(self, i: int) -> int:
        return self.dynarray[i]

    def set(self, i: int, n: int) -> None:
        # 'method' object cannot be interpreted as an integer error here
        self.dynarray[i] = n

    def pushback(self, n: int) -> None:
        if self.num_elements + 1 > self.capacity:
            self.resize()
        self.set(self.getSize(), n)
        self.num_elements+=1

    def popback(self) -> int:
        pop = self.dynarray[self.num_elements-1]
        self.dynarray[self.num_elements-1] = None
        self.num_elements-=1
        return pop

    def resize(self) -> None:
        self.dynarray.extend([None] * self.capacity)
        self.capacity*=2

    def getSize(self) -> int:
        return self.num_elements
    
    def getCapacity(self) -> int:
        return self.capacity
