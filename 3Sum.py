def threeSum(nums):
    if len(nums) < 3:
            return []

    nums = sorted(nums)

    output = set() 
    
    for i in range(len(nums)):
        left = i+1
        right = len(nums) - 1
        
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            
            if sum == 0 :
                output.add(tuple([nums[i],nums[left],nums[right]]))
                left += 1
           
            elif sum < 0 :
                left += 1
            else:
                right -= 1

    return output                     






if __name__ == "__main__":
    
    inputs  = [[-1,0,1,2,-1,-4],[0,1,1],[0,0,0]]
    
    for nums in inputs:
        print(threeSum(nums))    
        print("....................................") 
