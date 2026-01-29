https://www.geeksforgeeks.org/problems/count-digits5716/1

class Solution:
    def evenlyDivides(self, n):
        # code here
        num = n
        count=0
        n=str(n)
        
        for i in n:
            if int(i)==0:
                continue
            elif num % int(i) == 0:
                count+=1
        return count
