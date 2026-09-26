class stack:
    '栈'
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.empty():
            return self.items.pop()
    def back(self):
        if not self.empty():
            return self.items[-1]
    def top(self):
        if not self.empty():
            return self.items[0]
    def empty(self):
        return len(self.items) == 0
    def __repr__(self):
        return 'Stack' + str(self.items)
