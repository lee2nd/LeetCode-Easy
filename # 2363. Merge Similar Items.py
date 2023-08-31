class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        cnt = Counter(dict(items1))
        cnt += Counter(dict(items2))
        return sorted(cnt.items())

A = [[1,3],[2,2]]
dict(A)
# {1: 3, 2: 2}

dict(A).items()
# dict_items([(1, 3), (2, 2)])
