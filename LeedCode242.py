class Solution(object):
    def isAnagram(self, s, t):
        dict={}
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for j in t:
            if j in dict:
                dict[j]-=1
            else:
                return False
        for i in dict:
            if dict[i]!=0:
                return False
        return True