# from collection import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            group[key].append(word)

        return (group.values())