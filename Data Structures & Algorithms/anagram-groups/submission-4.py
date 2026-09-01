class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}

        for word in strs:
            chars = [0] * 26
            for char in word:
                chars[ord(char) - ord('a')] += 1
            key = tuple(chars)

            if key not in result:
                result[key] = []
            result[key].append(word)

        return list(result.values())