def minSubArrayLen2(target, nums):
        
        left = 0 
        right = 1 
        size = len(nums) + 1

        while right < len(nums)+1:

            window = nums[left:right]
        
            if sum(window) >= target:
                size = min(size,right-left) 
                left += 1
            else:
                right += 1 

        if size > len(nums): return 0 
        return size        

def minSubArrayLen(target, nums):
    
    min_length = len(nums)+1
    left = right = 0 
    
    while right < len(nums)+1:

        get_sum = sum(nums[left:right])
                
        if get_sum >= target:
            min_length = min(min_length,right-left)
            left +=1
        else:
            right +=1 
      
    if min_length > len(nums):
        return 0 
    return min_length                 

if __name__ == "__main__":
    inputs  = [[2,3,1,2,4,3],[1,4,4],[1,1,1,1,1,1,1,1],[1,2,3,4,5]]
    targets = [7,4,11,15]
    outputs = [2,1,0,5]

    for i in range(len(inputs)):
        nums = inputs[i]
        target = targets[i]
        result = minSubArrayLen(target, nums)
        if result == outputs[i]:
            print("Test Passed")
        else:
            print(f"{result} is not the correct answer . Correct is {outputs[i]} ")    


## Description
"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""