class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        self.pop_stack = []
        while len(self.main_stack) > 0:
            self.pop_stack.append(self.main_stack[-1])

        print(pop_stack)
        """
        ret_val = self.pop_stack.pop(0)
        
        self.main_stack = []        
        while len(self.pop_stack) > 0:
            self.main_stack.append(self.pop_stack[-1])

        return ret_val
        """
        return -1
    def peek(self) -> int:
        return self.main_stack[-1]

    def empty(self) -> bool:
        return len(self.main_stack) != 0 or len(self.pop_stack) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()