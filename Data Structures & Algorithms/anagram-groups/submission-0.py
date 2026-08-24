class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sorted keys will be common to string that are anagrams. Therefore loop through strs to then map it to the key, string, with the value being the the sorted key.
        common_key = {}

        for s in strs:
            # create a hashable key from sorted characters
            key = tuple(sorted(s))
            
            if key not in common_key:
                common_key[key] = [s]
            else:
                common_key[key].append(s)
        
            



        # for i in range(len(strs)):
        #     if sorted(strs[i]) not in common_key.keys():
        #         common_key[strs[i]] = sorted([str(strs[i])])
        #     elif sorted(strs[i]) in common_key.keys():
        #         common_key[strs[i]].add([str(strs[i])])
        #     else:
        #         return [[""]]

        return list(common_key.values())

