'''
数学集成库
数字范围 -1e100 - 1e100
'''
from math import *
from re import *
import random as rd
try:
    from numpy import *
except ImportError:
    pass
__all__ = ['A','C','stlasn','m3','m2','matrix_three','matrix_two','npow2']

def A(n,m):
    '''\
排列数:
 n
A  = m(m - 1)(m - 2)...(m - n + 1)
 m\
    '''
    s = 1
    for i in range(m - n + 1,m + 1):
        s *= i
    return s
def C(n,m):
    '''\
组合数:
 n    n    n
C  = A  - A
 m    m    n\
'''
    return A(n,m) - A(n,n)
def stlasn(*l):
    '''
Swap the largest and smallest numbers --- 交换序列最大最小数
'''
    assert len(l) > 0
    assert all(*[bool(type(e) == float or type(e) == int) for e in l])
    ma,mi = l[0],l[0]
    for i in range(1,len(l)):
        if l[i] > l[ma]:
            ma = i
        if l[i] < l[mi]:
            mi = i
    l[ma],l[mi] = l[mi],l[ma]
def npow2(n):
    return 1 if n == 1 else npow2(n - 1) + 2 * n - 1
def m3(a = 0,b = 0,c = 0):
    'matrix_three的快捷方式'
    return matrix_three(a,b,c)

def m2(a = 0,b = 0):
    'matrix_two的快捷方式'
    return matrix_two(a,b)

class matrix_three:
    '''3d多维矩阵的描述'''
    def __init__(self,a = 0,b = 0,c = 0,init_value = 0):
        self.width = a
        self.height = b
        self.length = c
        self.data = [[[init_value] * a] * b] * c
    def __add__(self,other):
        self.__assert_isinstance(other)
        return matrix_three(self.width + other.width,self.height + other.height,self.length + other.length)
    def __iadd__(self,other):
        self.__assert_isinstance(other)
        return matrix_three(self.width + other.width,self.height + other.height,self.length + other.length)
    def __eq__(self,other):
        self.__assert_isinstance(other)
        return (self.width * self.height * self.length == other.width * other.height * other.length)
    def __gt__(self,other):
        self.__assert_isinstance(other)
        return (self.width * self.height * self.length > other.width * other.height * other.length)
    def __ge__(self,other):
        self.__assert_isinstance(other)
        return (self.width * self.height * self.length >= other.width * other.height * other.length)
    def __repr__(self):
        return 'matrix_three(width = %g, height = %g, length = %g),and has data'%(self.width,self.height,self.length)
    def __int__(self):
        return int(self.sum_up())
    def sum_up(self):
        return self.width * self.height * self.length
    def discard(self):
        self.width = 0
        self.height = 0
        self.length = 0
        self.data = None
    def reset(self,**kw):
        t = ('width','height','length')
        assert len({k:v for k,v in kw.items()if k not in t}) < 1
        if 'width' in kw.keys():
            assert type(kw['width']) == float or type(kw['width']) == int
            self.width = kw['width']
        if 'height' in kw.keys():
            assert type(kw['height']) == float or type(kw['height']) == int
            self.height = kw['height']
        if 'length' in kw.keys():
            assert type(kw['length']) == float or type(kw['length']) == int
            self.length = kw['length']
        if self.data.__len__() > self.width:
            while len(self.data) > self.width:
                self.data.pop(-1)
    def clear_data(self,init_value = 0):
        self.data = [[[init_value] * self.length] * self.height] * self.width
    def __assert_isinstance(self,other):
        if not isinstance(other,matrix_three):
            raise TypeError('The addends must be of the same type.')

class matrix_two:
    '2d矩阵的描述'
    def __init__(self,a = 0,b = 0,init_value = 0):
        self.width = a
        self.height = b
        self.data = [[init_value] * a] * b
    def __add__(self,other):
        self.__assert_isinstance(other)
        return matrix_two(self.width + other.width,self.height + other.height)
    def __iadd__(self,other):
        self.__assert_isinstance(other)
        return matrix_two(self.width + other.width,self.height + other.height)
    def __eq__(self,other):
        self.__assert_isinstance(other)
        return (self.width * self.height == other.width * other.height)
    def __gt__(self,other):
        self.__assert_isinstance(other)
        return (self.width * self.height > other.width * other.height)
    def __ge__(self,other):
        self.__assert_isinstance(other)
        return (self.width * self.height >= other.width * other.height)
    def __repr__(self):
        return 'matrix_two(width = %g, height = %g),and has data'%(self.width,self.height)
    def __int__(self):
        return int(self.sum_up())
    def sum_up(self):
        return self.width * self.height
    def discard(self):
        self.width = 0
        self.height = 0
        self.data = None
    def reset(self,**kw):
        t = ('width','height')
        assert len({k:v for k,v in kw.items()if k not in t}) < 1
        if 'width' in kw.keys():
            assert type(kw['width']) == float or type(kw['width']) == int
            self.width = kw['width']
        if 'height' in kw.keys():
            assert type(kw['height']) == float or type(kw['height']) == int
            self.height = kw['height']
        self.data = [[0] * self.width] * self.height
    def clear_data(self,init_value = 0):
        self.data = [[init_value] * self.width] * self.height
    def __assert_isinstance(self,other):
        if not isinstance(other,matrix_two):
            raise TypeError('The addends must be of the same type.')
