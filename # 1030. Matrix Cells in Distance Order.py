# 雙層 list 寫法
# sort 雙層 list 裡面 by 內層 list 的 value

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def dist(point):
            pi, pj = point
            return abs(pi - r0) + abs(pj - c0)

        points = [(i, j) for i in range(R) for j in range(C)]
        return sorted(points, key=dist)

[(i, j) for i in range(3) for j in range(4)]
# [(0, 0),
#  (0, 1),
#  (0, 2),
#  (0, 3),
#  (1, 0),
#  (1, 1),
#  (1, 2),
#  (1, 3),
#  (2, 0),
#  (2, 1),
#  (2, 2),
#  (2, 3)]
