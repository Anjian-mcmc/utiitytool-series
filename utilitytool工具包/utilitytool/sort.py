'''一些排序算法'''
__all__ = ['sort','mergeSort','bubbleSort','insertionSort','quickSort','selectionSort','scrambleSort','reverse','bottleSort']

# 归并排序的几个函数
def mergeSort(arr):
    '''归并排序'''
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return _merge(left,right)
def _merge(left,right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# 冒泡排序
def bubbleSort(arr):
    '''冒泡排序'''
    n = len(arr)
    for i in range(n):
        for j in range(0,n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
    return arr

# 快速排序
def quickSort(arr):
    '''快速排序'''
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

# 插入排序
def insertionSort(arr):
    '''插入排序'''
    n = len(arr)
    for i in range(1,n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j],arr[j - 1] = arr[j - 1],arr[j]
            j -= 1
        arr[j],arr[i] = arr[i],arr[j]
    return arr

# 选择排序
def selectionSort(arr):
    '''选择排序'''
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:
                minIndex = j
    return arr

# 希尔排序
def scrambleSort(arr):
    '''希尔排序'''
    n = len(arr)
    for i in range(n):
        for j in range(i + 1,n):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

def reverse(arr,start = 0,end = -1):
    if(end == -1):
        end = len(arr) - 1
    return arr[:start] + arr[start:end + 1][::-1] + arr[end + 1:]

def bottleSort(arr):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

if __name__ == '__main__':
    pass