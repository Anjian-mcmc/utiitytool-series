import os as _os,time as _tm
__all__ = ['save','save_file']
class LineCanNotBeZeroError(Exception):
    pass
class ReadError(FileExistsError):
    pass
class WriteError(FileExistsError):
    pass
def save(data,path,mark,line = 1,encode = 'utf-8'):
    '''\
data:保存的数据
filepath:保存的文件路径
mark:保存行的标记
line:保存行离标记的行距离
encode:保存文件的编码
'''
    _tm.sleep(1)
    if line == 0:
        raise LineCanNotBeZeroError
    if not _os.path.isfile(path):
        raise FileExistsError
    try:
        with open(path,'r',True,encode) as f:
            l = f.readlines()
    except:
        return ReadError
    l.insert(0,'')
    index = l.index(mark + '\\n') + line
    l[index] = l[index].replace(l[l[index].index('=') + 2 : -1],data)
    try:
        with open(path,'w',True,encode) as f:
            f.write(''.join(l))
    except:
        return WriteError
    return (l,index)

class save_file:
    '便携式文件操作器'
    def __init__(self,path):
        if not _os.path.exists(path):
            raise FileNotFoundError
        self.path = _os.path.abspath(path)
    def delline(self,index1,index2 = None,ignore_line_breaks = False):
        s,l = '',[]
        with open(self.path,'r',True,'utf-8') as f:
            if ignore_line_breaks:
                for i in f.readlines():
                    l.append(i.strip('\n'))
            else:
                l = list(f.read())
        if index2 is None:
            s = l.pop(index1)
        else:
            for i in range(index1,index2 + 1):
                s += l.pop(index1)
        with open(self.path,'w',True,'utf-8') as f:
            if ignore_line_breaks:
                f.write('\n'.join(l))
            else:
                f.write(''.join(l))
        return s
    def delall(self):
        with open(self.path,'w',True,'utf-8') as f:
            f.write('')
    def read(self,start = None,char = None):
        with open(self.path,'r',True,'utf-8') as f:
            if char is None:
                if start is None or start <= 1:
                    s = f.read()
                else:
                    f.read(start - 1)
                    s = f.read()
            else:
                if start is None:
                    s = f.read(char)
                else:
                    f.read(start - 1)
                    s = f.read(char)
        return s
    def readline(self,line = None,ignore_line_breaks = False):
        with open(self.path,'r',True,'utf-8') as f:
            if line is None or line <= 1:
                if ignore_line_breaks:
                    s = f.readline().strip('\n')
                else:
                    s = f.readline()
            else:
                for i in range(line - 1):
                    f.readline()
                if ignore_line_breaks:
                    s = f.readline().strip('\n')
                else:
                    s = f.readline()
        return s
    def readlines(self,ignore_line_breaks = False):
        l = []
        with open(self.path,'r',True,'utf-8') as f:
            if ignore_line_breaks:
                for i in f.readlines():
                    l.append(i.strip('\n'))
            else:
                l = f.readlines()
        return l
    def write(self,char,writechar = 'all',pointer = 0,mode = 'insert'):
        with open(self.path,'r',True,'utf-8') as f:
            s = f.read()
        with open(self.path,'w',True,'utf-8') as f:
            r = s[:pointer] + char
            if writechar != 'all':
                if mode == 'insert':
                    r = r + s[pointer:]
                elif mode == 'cover':
                    r = r + s[pointer + len(char):]
                else:
                    raise ValueError('mode must be insert or cover')
            f.write(r)
    def __repr__(self):
        return self.path + ' 的便携式文件操作器'
