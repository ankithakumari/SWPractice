strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for item in strs:
            key = ''.join(sorted(item))
            if key not in hashmap:
                hashmap[key] = [item]
            else:
                hashmap[key].append(item)
        return list(hashmap.values())
       
        

print(groupAnagrams(strs))