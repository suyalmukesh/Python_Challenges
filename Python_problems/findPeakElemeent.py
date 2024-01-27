def findPeakElement1(nums):
    # Brute Force . This is O(n). Accepted by Leetcode 
    # Edge cases 
    if len(nums) == 1: return 0 
    if nums[0] > nums[1]: return 0 
    if nums[len(nums)-1] > nums[len(nums)-2]: return len(nums)-1 
    peak = []    
    for i in range(1,len(nums)-1):

        prev = nums[i-1]
        next = nums[i+1]

        if nums[i] > prev and nums[i] > next:
            peak.append(i)
    return peak

def findPeakElement2(nums):

    left = 0 
    right = len(nums) - 1

    while left < right:
        
        mid = int(left + (right - left )/2)

        if nums[mid] > nums[mid+1]:
            right = mid 
        else:
            left = mid+1
    
    return left             

    

if __name__ == "__main__":
    inputs = [[1,2,3,1],[1,2,1,3,5,6,4],[1]]

    for nums in inputs:
        print(f"Peak Element (BF) : {findPeakElement1(nums)}")
        print(f"Peak Element (O) : {findPeakElement2(nums)}")



