class __array_metaclasses(type):
    def __new__(cls,name,bases,attrs):
        def __ge__(self,other):
            assert isinstance(self,other)
            return self.sum_up() >= other.sum_up()
        def __eq__(self,other):
            assert isinstance(self,other)
            return self.sum_up() == other.sum_up()
        def __gt__(self,other):
            assert isinstance(self,other)
            return self.sum_up() > other.sum_up()
        
        attrs['__ge__'] = __ge__
        attrs['__eq__'] = __eq__
        attrs['__gt__'] = __gt__
        attrs['__ne__'] = lambda self,other:not __eq__(self,other)
        attrs['__lt__'] = lambda self,other:not __gt__(self,other)
        attrs['__le__'] = lambda self,other:not __ge__(self,other)
        return type.__new__(cls,name,bases,attrs)
