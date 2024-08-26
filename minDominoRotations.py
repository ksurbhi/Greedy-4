class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(1), as dice only have 6 sides so we will only store 6 nubers in our hashmap
    """
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(tops)==0 or len(bottoms)==0:
            return -1
        hashmap = {}
        target = -1
        for i in range(len(tops)):
            t = tops[i]
            if t not in hashmap:
                hashmap[t] = 0
            hashmap[t] +=1
            if hashmap[t] == len(tops):
                target = t
                break
            b = bottoms[i]
            if b not in hashmap:
                hashmap[b] = 0
            hashmap[b] +=1
            if hashmap[b] == len(tops):
                target = b
                break
        if target == -1:
            return -1
        return self.findMinRotations(tops,bottoms,target)
    
    def findMinRotations(self,tops: List[int], bottoms: List[int],target:int) -> int:
        topRotations = 0
        bottomRotations = 0
        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return -1
            if tops[i] != target:
                topRotations +=1
            if bottoms[i] != target:
                bottomRotations +=1
        return min(topRotations,bottomRotations)





        
