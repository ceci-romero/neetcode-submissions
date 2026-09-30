class MinStack:

    def __init__(self):
       self.stack = [] 
       
    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return min(self.stack)
            # min = self.stack[0]
            # for i in self.stack:
            #     if i < min:
            #         min = i
            # return min
        
        
