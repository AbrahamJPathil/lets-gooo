class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arrIndex = -1
        minIndex = 0
        maxIndex = len(matrix) - 1
        while(minIndex <= maxIndex):
            mid = int((minIndex + maxIndex)/2)
            minRange = matrix[mid][0]
            maxRange = matrix[mid][-1]
            if(target >= minRange and target <= maxRange):
                arrIndex = mid
                break
            elif(target > maxRange):
                minIndex += 1
            else:
                maxIndex -= 1
        
        if(arrIndex == -1):
            return False


        arr = matrix[arrIndex]
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
        