class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1
        pairs = list(freqDict.items())
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        return [pair[0] for pair in sorted_pairs[-k:]]