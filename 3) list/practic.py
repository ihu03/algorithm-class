class Stacck:
    def __init__(self,capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [None]*capacity

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity -1
    
    def push(self, item):
        if not self.isFull():
            self.array[self.top] = item
            print(f"{item}push 됨")
        else:
            print("꽉찻다잇")

    def pop(self):
        if not self.isEmpty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            return item
        else:
            print("꽉차 브렸으")

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        return None
    
    def size(self):
        if not self.isEmpty():
            return self.top+1
        else:
            print("비었음")


    
