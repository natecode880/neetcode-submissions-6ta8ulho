class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        sorted_output = []
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        sorted_output = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

        return list(sorted_output[0:k])