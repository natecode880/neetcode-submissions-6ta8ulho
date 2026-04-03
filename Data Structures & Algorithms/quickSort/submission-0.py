# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs: List[Pair], start: int, end: int) -> None:
        if start >= end:
            return
        
        pivot_idx = self.partition(pairs, start, end)

        #left side of the partition (pivot index - elements >= pivot)
        self.quickSortHelper(pairs, start, pivot_idx - 1)

        #right side of the partition (pivot index - elements < pivot)
        self.quickSortHelper(pairs, pivot_idx + 1, end)


    def partition(self, pairs: List[Pair], s: int, e: int) -> int:
        pivot = pairs[e]
        left = s #pointer for left side

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                temp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = temp
                left+= 1

        #swap pivot with the larger value at i
        temp = pairs[left]
        pairs[left] = pairs[e]
        pairs[e] = temp

        return left