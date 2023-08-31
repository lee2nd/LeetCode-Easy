# https://openhome.cc/zh-tw/python/flow-control/match-case/

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
