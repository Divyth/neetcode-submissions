
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        # Step 1: Store frequency of s1
        freq1 = Counter(s1)
        
        # Step 2: Sliding window frequency map
        window = Counter()
        
        left = 0
        
        for right in range(len(s2)):
            
            # Add current character
            window[s2[right]] += 1
            
            # If window size exceeds len(s1), shrink it
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                
                # Remove zero frequency keys (important!)
                if window[s2[left]] == 0:
                    del window[s2[left]]
                
                left += 1
            
            # Compare both maps
            if window == freq1:
                return True
        
        return False
        