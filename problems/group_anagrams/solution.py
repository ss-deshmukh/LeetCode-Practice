class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        group_lookup = {}
        unq_val_cntr = 0
        
        for e in strs:

            count = [0] * 26
            for char in e:
                count[ord(char) - 97] += 1

            key = tuple(count)
            if key not in group_lookup:
                group_lookup[key] = unq_val_cntr
                unq_val_cntr += 1
                result.append([e])
            else:
                result[group_lookup[key]].append(e)
                
        return result