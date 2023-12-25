def summaryRanges(nums):
    
    if len(nums) == 0 : return []
    tmp_list = []
    output = []
    n = len(nums)
    left = nums[0]
    right = nums[0]

    for i in range(1,n):    
       
        if nums[i] - nums[i-1] == 1:
            right = nums[i]
                    
        else:
            tmp_list.append([left,right])
            left = nums[i]
            right = nums[i]
    tmp_list.append([left,right])    

  
    for bracket in tmp_list:
        left = bracket[0]
        right = bracket[1]
        if left == right:
            st = str(left)
        else:
            st = str(left) + "->" + str(right)    
        output.append(st)
    return output 

if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    print(summaryRanges(nums))
    nums = [0,2,3,4,6,8,9]
    print(summaryRanges(nums))
    nums = []
    print(summaryRanges(nums))
    nums = [0]
    print(summaryRanges(nums))


        
