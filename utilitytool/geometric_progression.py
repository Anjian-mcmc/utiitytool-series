'等比数列'
#import functools as func
__all__ = ['geometric_progression']
#@func.total_ordering
from .__array_metaclasses import __array_metaclasses as __ames
class geometric_progression(metaclass = __ames):
    '等比数列'
    def __init__(self,start = 1,end = 10,step = '2*',roun = True):
        '''\
step:一个字符串,4*表示前后的比为1:4;4/表示表示前后的比为4:1
roun:表示是否四舍五入\
'''
        f = step[1]
        assert f == '*' or f == '/'
        assert type(roun) == bool
        step = int(step[0])
        self.list = [0]
        i = start
        while (i <= end if f == '*' else i >= end):
            self.list.append(i)
            if f == '*':
                i = round(i * step) if roun else i * step
            else:
                i = round(i / step) if roun else i / step
        self.start = start
        self.len = len(self.list)
        self.step = str(step) + str(f)
    def sum_up(self,start = 0,end = None,bi = 1):
        if end == None:
            end = self.len
        return sum(self.list[start:end + 1])
    def __repr__(self):
        return 'geometric_progression[(%s),start = %d,len = %d,end = %d,step = %s,sum = %d]'\
               %(','.join(map(str,self.list)),self.start,self.len,self.list[-1],self.step,self.sum_up())
                                    
if __name__ == '__main__':
    a = geometric_progression(start = 1,end = 100,step = '2*')
    print(a)
