class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        b=[]
        for i in range(len(nums)):
            if(nums[i]==target):
                b.append(i)
        if(len(b)>=1):
            c=b[0]
            d=b[-1]
            return [c,d]
        else:
            return[-1,-1]
        
        
            
            
        
                
                
        
