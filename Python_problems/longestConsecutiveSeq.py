def longestConsecutive1(nums):
    if len(nums) == 0 : return 0 
    out = []
    nums = sorted(nums)
    temp = [nums[0]]

    for i in range(1,len(nums)):
        if nums[i] - nums[i-1] == 0:
            pass
        elif nums[i] - nums[i-1] == 1:
            temp.append(nums[i])
        else:
            out.append(temp)
            temp = []
            temp.append(nums[i])
                
    out.append(temp)
    return max([len(x) for x in out])


# Make a note of this solution , really small and efficient 
def longestConsecutive(nums):
    
    numSet = set(nums)
    longest = 0 

    for n in nums:
        if n-1 not in numSet:
            length = 0 
            while (n + length) in numSet:
                length += 1
            longest = max(longest,length)
    
    return longest            





    
 


if __name__ == "__main__":

    inputs = [[100,4,200,1,3,2],[0,3,7,2,5,8,4,6,0,1],[0, 0, 1, 2, 3, 4, 5, 6, 7, 8]]
    for nums in inputs:
        print(longestConsecutive1(nums))
        print(longestConsecutive(nums))
