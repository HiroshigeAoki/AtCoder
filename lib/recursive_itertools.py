# https://qiita.com/BlueSilverCat/items/77f4e11d3930d7b8959b


def _listExcludedIndices(data, indices=[]):
    """一度取り出してものを覗いたリストを返す"""
    return [x for i, x in enumerate(data) if i not in indices]

def permutationWithRepetitionListRecursive(data, r):
    """重複あり順列"""
    if r <= 0:
        return []
    result = []
    _permutationWithRepetitionListRecursive(data, r, [], result)
    return result

def _permutationWithRepetitionListRecursive(data, r, progress, result):
    if r == 0:
        result.append(progress)
        return

    for i in range(len(data)):
        _permutationWithRepetitionListRecursive(data, r - 1, progress + [data[i]], result)

def permutationListRecursive(data, r):
    """順列（重複なし）"""
    if r <= 0 or r > len(data):
        return []

    result = []
    _permutationListRecursive(data, r, [], result)
    return result

def _permutationListRecursive(data, r, progress, result):
    if r == 0:
        result.append(progress)
        return

    for i in range(len(data)):
        _permutationListRecursive(_listExcludedIndices(data, [i]), r - 1, progress + [data[i]], result)

def combinationWithRepetitionListRecursive(data, r):
    """組み合わせ（重複あり）"""
    if r <= 0:
        return []

    result = []
    _combinationWithRepetitionListRecursive(data, r, 0, [], result)
    return result

def _combinationWithRepetitionListRecursive(data, r, start, progress, result):
    if r == 0:
        result.append(progress)
        return

    for i in range(start, len(data)):
        _combinationWithRepetitionListRecursive(data, r - 1, i, progress + [data[i]], result)

def combinationListRecursive(data, r):
    """組み合わせ（重複なし）"""
    if r == 0 or r > len(data):
        return []

    result = []
    _combinationListRecursive(data, r, 0, [], result)
    return result

def _combinationListRecursive(data, r, start, progress, result):
    if r == 0:
        result.append(progress)
        return

    for i in range(start, len(data)):
        #別解 _combinationListRecursive(listExcludedIndices(data, [i]), r - 1, i, progress + [data[i]], result)
        _combinationListRecursive(data, r - 1, i + 1, progress.append(data[i]), result)