# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

# method 1 - 超過 time complexity
[i for i in self.requests if i>=interval[0] and i<=interval[1]]

# method 2 - 超過 time complexity
list(filter(lambda x:x>=interval[0] and x<=interval[1], self.requests))

# method 3 - 用 deque()，讓儲存 t 的 list 不會無限長大
# https://www.geeksforgeeks.org/deque-in-python/
