class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}                       # sorted letters -> list of words

        for word in strs:
            key = "".join(sorted(word))   # "eat", "tea", "ate" all become "aet"
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())