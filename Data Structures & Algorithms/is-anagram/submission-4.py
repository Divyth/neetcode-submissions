class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S_counter = Counter(s)
        T_counter = Counter(t)
        #A type of Hashmap called Counter: which is used to keep 
        # track of counters
        return S_counter == T_counter
#        for l in t:
 #           if l not in counter or counter[l] == 0:
  #              return False
   #         counter[l] -=1
    #    return True 


                