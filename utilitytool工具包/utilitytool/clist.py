__all__ = ['clist']
class clist(list):
    def __init__(self,*args):
        list.__init__(self,*args)
        del self.append,self.insert,self.extend,self.pop,self.__delitem__,\
            self.remove,self.clear,self.reverse
        def a(self):
            for i in range(len(self)):
                self[i] = 0
        self.clear = a
        del a