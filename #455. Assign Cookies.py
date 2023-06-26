class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        cookie, kid, count = 0, 0, 0
        while cookie < len(s) and kid < len(g):
            if s[cookie] >= g[kid]:
                cookie += 1
                kid += 1
            else:
                cookie += 1
        return kid
