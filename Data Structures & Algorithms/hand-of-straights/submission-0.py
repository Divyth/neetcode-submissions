class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for num in sorted(count):
            while count[num] > 0:
                
                for i in range(groupSize):
                    curr = num + i

                    if count[curr] == 0:
                        return False
                    
                    count[curr] -= 1
        return True
        