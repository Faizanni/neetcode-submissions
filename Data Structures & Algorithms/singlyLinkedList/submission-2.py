class Node:
    def __init__(self, val, next_node):
        self.val = val
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.num_elements = 0
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if index >= self.num_elements:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next_node
        return curr.val


    def insertHead(self, val: int) -> None:
        new = Node(val, None)
        if self.num_elements == 0:
            self.tail = new
        else:
            new.next_node = self.head
        self.head = new
        self.num_elements+=1


    def insertTail(self, val: int) -> None:
        new = Node(val, None)
        if self.num_elements == 0:
            self.head = new
        else:
            self.tail.next_node = new
        self.tail = new
        self.num_elements+=1


    def remove(self, index: int) -> bool:
        if index >= self.num_elements:
            return False
        if self.num_elements == 1:
            self.head = None
            self.tail = None
            self.num_elements-=1
            return True
        if index==0:
            self.head = self.head.next_node
            self.num_elements-=1
            return True

        curr = self.head
        prev = None
        for i in range(index):
            prev = curr
            curr = curr.next_node

        if curr == self.tail:
            self.tail = prev
        prev.next_node = curr.next_node
        self.num_elements-=1
        return True


    def getValues(self) -> List[int]:
        curr = self.head
        if self.num_elements == 0:
            return []
        vals = list()
        while True:
            vals.append(curr.val)
            curr = curr.next_node
            if not curr:
                break
        return vals      
