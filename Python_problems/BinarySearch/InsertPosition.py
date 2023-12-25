def searchInsert(nums, target):

    left , right = 0 , len(nums) - 1

    while left <= right:
        mid = int((right + left) / 2)

        if target == nums[mid]:
            return mid 
        
        if target < nums[mid]:
            right = mid - 1
        
        else:
            left = mid + 1

    return left 



if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    Output = 2
    collect = searchInsert(nums, target)
    if Output == collect:
        print("Correct")
    else: 
        print(f"{collect} is NOT the correct answer ")

    nums = [1,3,5,6]
    target = 2
    Output = 1
    collect = searchInsert(nums, target)
    if Output == collect:
        print("Correct")
    else: 
        print(f"{collect} is NOT the correct answer ")
    

    nums = [1,3,5,6]
    target = 7
    Output = 4
    collect = searchInsert(nums, target)
    if Output == collect:
        print("Correct")
    else: 
        print(f"{collect} is NOT the correct answer ")