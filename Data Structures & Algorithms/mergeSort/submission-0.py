
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        startIndex = 0
        middleIndex = len(pairs) // 2
        endIndex = len(pairs) - 1

        if len(pairs) <= 1:
            return pairs

        leftSubArray = pairs[:middleIndex]
        rightSubArray = pairs[middleIndex:]

        #sort left subarray
        sorted_left = self.mergeSort(leftSubArray)

        #sort right subarray
        sorted_right = self.mergeSort(rightSubArray)

        return self.merge(sorted_left, sorted_right)

    def merge(self, leftSubArray, rightSubArray) -> None:
        merged = []
        left_arr_index = right_arr_index = 0
        
        while left_arr_index < len(leftSubArray) and right_arr_index < len(rightSubArray):
            if leftSubArray[left_arr_index].key <= rightSubArray[right_arr_index].key:
                merged.append(leftSubArray[left_arr_index])
                left_arr_index += 1
            else:
                merged.append(rightSubArray[right_arr_index])
                right_arr_index += 1
        
        while left_arr_index < len(leftSubArray):
            merged.append(leftSubArray[left_arr_index])
            left_arr_index += 1

        while right_arr_index < len(rightSubArray):
            merged.append(rightSubArray[right_arr_index])
            right_arr_index += 1

        return merged