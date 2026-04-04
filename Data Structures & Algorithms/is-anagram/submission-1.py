from collections import defaultdict, Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # Two ways to fail
    # 1. different keys
    # 2. same keys different counts
        freqs1 = defaultdict(int)
        freqs2 = defaultdict(int)
        freqs1 = Counter(s)
        freqs2 = Counter(t)
        
        merged = dict(freqs1 + freqs2)

        for k, v in merged.items():
            # in case of anagram the count must be even
            if v%2 != 0:
                return False
            else:
                # the summed count has to be double of one of the individual counts
                if (v == 2*freqs1[k]) or (v == 2*freqs2[k]):
                    continue
                else:
                    return False 
        return True

        
        