class Solution:
    """
    Time Complexity: m*n
    Space Complexity: O(1)
    """
    def shortestWay(self, source: str, target: str) -> int:
        if source == target:
            return 0
        if len(source) == 0 and source == None:
            return -1
        count = 1
        char_set = set()
        for c in source:
            char_set.add(c)
        tp = 0 #target pointer
        sp= 0 # source pointer
        while tp < len(target):
            c = target[tp]
            if c not in char_set:
                return -1
            if target[tp] == source[sp]:
                sp = sp+1
                tp = tp +1
            else:
                sp = sp+1
            if sp == len(source) and tp < len(target):
                sp = 0
                count +=1
        return count



########## Method 2##############
class Solution:
    """
    Time Complexity: (m + nlog m)
    Space Complexity: O(1)
    """
    def shortestWay(self, source: str, target: str) -> int:
        if source == target:
            return 0
        if len(source) == 0 and source == None:
            return -1
        count = 1
        char_dict = collections.defaultdict(list)
        for index, char in enumerate(source):
            char_dict[char].append(index)
        tp = 0 #target pointer
        sp= 0 # source pointer
        while tp < len(target):
            c = target[tp]
            if c not in char_dict:
                return -1
            li = char_dict[c]
            k = bisect.bisect_left(li,sp)
            if  k == len(li):
                sp = 0
                count +=1
            else:
                sp = li[k] +1
                tp +=1
        return count
         

        
