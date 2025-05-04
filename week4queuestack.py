class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    def push(self, x):
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        self.stack_in.append(x)
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())
    def pop(self):
        return self.stack_in.pop()
    def peek(self):
        return self.stack_in[-1]
    def empty(self):
        return not self.stack_in
