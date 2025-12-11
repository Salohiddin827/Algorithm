class Solution:
    def TwoSum(self,num, target):
        seen = {}
        for i, n in enumerate(num):
            need = target - n
            if need in seen:
                return [seen[need],i]
            seen[n] = i