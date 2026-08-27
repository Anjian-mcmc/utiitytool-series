class stack:
    '栈'
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def end(self):
        if not self.is_empty():
            return self.items[-1]
    def none(self):
        return len(self.items) == 0
    def is_empty(self):
        return len(self.items) == 0
    def empty(self):
        return self.is_empty()
    def __repr__(self):
        return self.items.__repr__()
