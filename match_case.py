# leetcode 2347. Best Poker Hand

# "Flush": Five cards of the same suit.
# "Three of a Kind": Three cards of the same rank.
# "Pair": Two cards of the same rank.
# "High Card": Any single card.

# Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
# Output: "Flush"

if len(set(suits)) == 1:
    return "Flush"
match max(Counter(ranks).values()):
    case 3 | 4 | 5:
        return "Three of a Kind"
    case 2:
        return "Pair"
    case _:
        return "High Card"

# https://openhome.cc/zh-tw/python/flow-control/match-case/

text = 'hi'
match text:
    case 'hi':
        print('嗨')
    case 'hello':
        print('哈囉')
        
lt = [3, 4]
match lt:
    case [1, 2]:
        print('三')
    case [3, 4]:
        print('七')
        
dt = {'x': 10, 'y': 20}
match dt:
    case {'x': 0, 'y': 0}:
        print('原點')
    case {'x': x, 'y': y}:
        print((x, y))
