# https://www.geeksforgeeks.org/problems/third-largest-element/1

class Solution:
    def thirdLargest(self, arr):
        distinct = sorted(set(arr))  # Remove duplicates and sort
        if len(distinct) < 3:
            return -1
    
        return distinct[-3]  # Third largest from the end