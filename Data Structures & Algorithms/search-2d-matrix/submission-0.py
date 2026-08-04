class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for arr in matrix:
            start = 0
            end = len(arr) - 1
            while(start <= end):
                mid = int((start + end)/2)
                if(arr[mid] == target):
                    return True    
                elif(arr[mid] > target):
                    end = mid - 1
                else:
                    start = mid + 1
            
        return False
        