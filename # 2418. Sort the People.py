class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_dict = dict(zip(heights,names)) # // height_dict = {180: 'Mary', 165: 'John', 170: 'Emma'}
        names.clear()
        for key in sorted(height_dict.keys(),reverse=True):
            names.append(height_dict[key])
        return names

# 要讓 names = ["Mary","John","Emma"], heights = [180,165,170] 變成 {180: 'Mary', 165: 'John', 170: 'Emma'} 可用以下方法:
height_dict = dict(zip(heights,names))
