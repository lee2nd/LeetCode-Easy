1. First, sort both the array of children's greed factors and the array of cookie sizes in ascending order.
2. Initialize two variables, one for the index of the smallest cookie and one for the index of the least greedy child, both starting at 0.
3. Now, loop through both arrays, checking if the current cookie can satisfy the current child. If it can, increment both the cookie index and the child index. If it can't, increment only the child index.
4. Keep track of the number of children that have been satisfied and return it.

Here's the Python code for this solution:

def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    i, j = 0, 0
    count = 0
    while i < len(s) and j < len(g):
        if s[i] >= g[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count

In this code, g is the array of children's greed factors, and s is the array of cookie sizes. The function returns the maximum number of satisfied children.
