'等差数列'
#import functools as func
__all__ = ['arithmetic_sequence']
#@func.total_ordering
from .__array_metaclasses import __array_metaclasses as __ames
class arithmetic_sequence(metaclass = __ames):
    '等差数列'
    def __init__(self,start = 0,end = 10,step = 1,length = None):
        self.list = []
        if length is not None and (length - 1) * step + start > end:
            self.list = [e for e in range(start,(length - 1) * step + start + 1,step)]
        else:
            self.list = [e for e in range(start,end + 1,step)]
        if len(self.list) < 1:
            self.list = [0]
        self.len = len(self.list)
        self.start = start
        self.end = self.list[-1]
        self.step = step
    def sum_up(self,start = 0,end = None):
        if end == None:
            end = self.len
        return sum(self.list[start:end + 1])
    def __repr__(self):
        li,le,start,end,step = self.list,self.len,self.start,self.end,self.step
        return 'arithmetic_sequence[(%s),len = %d,start = %f,end = %f,sum = %g,step = %f]'%(', '.join(map(str,li)),\
                                    le,start,end,self.__float__(),step)
if __name__ == '__main__':
    a = arithmetic_sequence(start = 1,end = 100,step = 5)
    print(a)
