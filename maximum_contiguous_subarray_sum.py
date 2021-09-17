class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=res=nums[0]
        '''Traverse all elements of list and at given element we will check if sum till now is greater the current element if not then we consider 
        sum as current element and check the same for next element till last element.
        
        Time Complexity : O(n) '''
        
        for i in range(1,len(nums)):
            s = max(s+nums[i],nums[i])
            res=max(res,s)
        
        return res
