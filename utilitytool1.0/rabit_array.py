#import functools as func
__all__ = ['rabit_array']
#@func.total_ordering
from .__array_metaclasses import __array_metaclasses as __ames
class rabit_array(metaclass = __ames):
    '斐波那契数列'
    def __init__(self,length = 0):
        self.list = [0]
        fir,sec = 0,1
        for i in range(1,length):
            self.list.append(sec)
            sec = fir + sec
            fir = self.list[i]
        self.len = length
    def sum_up(self,start = 0,end = None):
        if end == None:
            end = self.len
        return sum(self.list[start:end + 1])
    def __getitem__(self,slice_):
        return self.list.__getitem__(slice_)
    def __repr__(self):
        return 'rabit_array[(%s),len = %d,end = %d,sum = %d]'%(','.join(map(str,self.list)),self.len,self.list[-1],self.sum_up())
    def __len__(self):
        return self.len

if __name__ == '__main__':
    a = rabit_array()
    input(a)
