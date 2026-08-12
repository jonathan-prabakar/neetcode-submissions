class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            groups.setdefault(key, []).append(strs[i])
        return list(groups.values())




