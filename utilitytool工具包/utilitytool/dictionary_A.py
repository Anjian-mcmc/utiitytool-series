__all__ = ['dictionary_all_A1']
#所有全排列
def dictionary_all_A1(arr):
    lst = arr.copy()
    res = []
    while lst != arr:
        for i in range(len(arr) - 1):
            lst[i + 1],lst[i] = lst[i], lst[i + 1]
            res.append(lst.copy())
    return tuple(*res)