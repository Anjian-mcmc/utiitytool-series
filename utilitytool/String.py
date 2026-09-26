__all__ = ['String']
class String:
    def get(self):
        return self.__str
    def __getother(self,other):
        return other if isinstance(str,other) else other.get()
    def __init__(self,string = ''):
        self.__str = string
        self.__doc__ = '可变str'
        self.__repr__ = self.__str.__repr__
        self.__iter__ = self.__str.__iter__
        self.__next__ = self.__str.__next__
    def __assert(self,other):
        assert isinstance(other,(str,String))
    def __add__(self,other):
        self.__assert()
        return self.__str + self.__getother(other)
    def __radd__(self,other):
        self.__assert()
        return self.__getother(other) + self.__str
    def __iadd__(self,other):
        self.__assert()
        self.__str = self.__str + self.__getother(other)
    def __sub__(self,other):
        self.__assert()
        index = self.find(self.__getother(other))
        assert index != -1
        return self.__str[:index] + self.__str[index + 1:]
    def __rsub__(self,other):
        self.__assert()
        other = self.__getother(other)
        index = other.find(self.__str)
        assert index != -1
        return other[:index] + other[index + 1:]
    def __isub__(self,other):
        self.__assert()
        index = self.find(self.__getother(other))
        assert index != -1
        self.__str = self.__str[:index] + self.__str[index + 1:]
    def __eq__(self,other):
        return self.__str == self.__getother(other)
    def __gt__(self,other):
        other = self.__getother(other)
        for i in range(min(len(other),len(self.__str))):
            if other[i] > self.__str[i]:
                return False
            elif other[i] != self.__str[i]:
                return True
        return False
    def __ge__(self,other):
        other = self.__getother(other)
        for i in range(min(len(other),len(self.__str))):
            if other[i] > self.__str[i]:
                return False
            elif other[i] != self.__str[i]:
                return True
        return True
    def __lshift__(self,other,fill = ' '):
        return self.__str + fill * other
    def __rshift__(self,other):
        return self.__str[:len(self.__str) - other]
    def __ilshift__(self,other,fill = ' '):
        self.__str = self.__str + fill * other
    def __irshift__(self,other):
        self.__str = self.__str[:len(self.__str) - other]
    def __mul__(self,other):
        return self.str * other
    def __imul__(self,other):
        self.__str = self.__str * other
    def __reversed__(self):
        self.__str = self.__str[::-1]
        return self.__str
    def reverse(self,other):
        self.__reversed__()
    def __len__(self):
        return len(self.__str)
    def __delitem__(self,slice_):
        self.__str = ''.join(list(self.__str).__delitem__(slice_))
    def __setitem__(self,slice_,d):
        self.__str = ''.join(list(self.__str).__setitem__(slice_,d))
    def __getitem__(self,slice_):
        return self.__getitem__(slice_)
    def __str__(self):
        return self.__str
