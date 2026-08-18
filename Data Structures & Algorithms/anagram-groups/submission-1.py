class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniqueStrings = {}
        result = []
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in uniqueStrings:
                result[uniqueStrings[sortedString]].append(string)
            else:
                result.append([string])
                uniqueStrings[sortedString] = len(result) - 1
        return result
            
