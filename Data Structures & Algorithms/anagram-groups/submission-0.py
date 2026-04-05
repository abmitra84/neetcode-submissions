from collections import defaultdict, Counter
import string
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # counts = []

        # # for s in strs:
        # #     counts.append(Counter(s))

        # # print(counts)
        # alpha_dict = {l:0 for l in string.ascii_lowercase}
        # signatures = []
        # for s in strs:
        #     alpha_dict[s] = strs.count(s)
        #     signatures.append(alpha_dict)
        # print(len(signatures))
        # print(signatures)

        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1  # setting a index corresponding to the char in alphabet to 1
            
            print("tuple : ", tuple(count))
            res[tuple(count)].append(s)

        
        return list(res.values())


        