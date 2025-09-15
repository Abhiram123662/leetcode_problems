class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashSet = {}
        matched = 0
        for ch in s:
            if ch not in hashSet:
                hashSet[ch] = 0
            hashSet[ch] += 1
        for ch in t:
            if ch not in hashSet:
                return False
            hashSet[ch] -= 1
            if hashSet[ch] < 0:
                return False
            elif hashSet[ch] == 0:
                matched += 1
        if matched == len(hashSet):
            return True
        else:
            return False
 



