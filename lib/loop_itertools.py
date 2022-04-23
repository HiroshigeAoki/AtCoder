# https://qiita.com/BlueSilverCat/items/77f4e11d3930d7b8959b
import math
import functools
import operator


def permutation(n, r):
    """順列の個数を返す"""
    if(n < r):
        return 0
    return int(math.factorial(n) / math.factorial(n - r))

def permutationList(data, r):
    """順列の組み合わせを返す"""
    length = len(data)
    total = permutation(length, r)
    result = []
    for i in range(total):
        element = []
        copyData = data[:]
        for _ in range(r):
            l = len(copyData)
            countUp = total / functools.reduce(operator.mul, range(l, length + 1))
            index = int(i / countUp) % l
            element.append(copyData.pop(index))
        result.append(element)
    return result


def combinationWithRepetition(n, r):
    """組み合わせの個数を返す"""
    return int(math.factorial(r + n - 1) / (math.factorial(r) * math.factorial(n - 1)))

def _updateCombinationIndex(lastIndex, start, repetition=False):
    result = lastIndex[:start]
    x = lastIndex[start] + 1
    for i in range(start, len(lastIndex)):
        result.append(x)
        if(repetition == False):
            x += 1
    return result

def _getComginationWithRepetitionIndex(length, r, lastIndex):
    result = []
    for i in range(r):
        if(len(lastIndex) == 0):
            result.append(0)
        elif(lastIndex[i] >= length - 1):
            result = _updateCombinationIndex(lastIndex, i - 1, True)
            break
        elif(i == r - 1):
            result = _updateCombinationIndex(lastIndex, i, True)
    return result

def _getListElements(lis, indices):
    """listからindicesで示される要素の組を返す"""
    return [lis[i] for i in indices]

def combinationWithRepetitionList(data, r):
    """組み合わせ（重複なし）"""
    length = len(data)
    total = combinationWithRepetition(length, r)
    result = []
    lastIndex = []
    for i in range(total):
        lastIndex = _getComginationWithRepetitionIndex(length, r, lastIndex)
        result.append(_getListElements(data, lastIndex))
    return result