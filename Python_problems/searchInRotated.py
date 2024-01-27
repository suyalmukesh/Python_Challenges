def search1(nums, target):
    
    ## Complexity :: O(n)
    for i in range(len(nums)):
        if nums[i] == target:
            return i 
    return -1 


def search2(nums,target):

    left = 0 
    right = len(nums) - 1
    pivot = 0 
    # Find Pivot
    while left < right:
       mid = int((left+right)/2)

       if nums[mid] > nums[mid+1]:
           pivot = mid
           print(f"Pivot position is {mid} and value is {nums[mid]}")
           return pivot  

       elif nums[mid] < nums[right]:
           right = mid - 1

       else:
           left = mid + 1

    if target 
















if __name__ == "__main__":
    numers  = [[4,5,6,7,0,1,2],[4,5,6,7,0,1,2],[1]]
    targets = [0,3,0]
    
    count = 0 
    for i in range(len(numers)):
       nums = numers[i]
       target = targets[i]
       count += 1
       print(f"Brute Force {count} : {search1(nums, target)}")
       print(f"Brute Force {count} : {search2(nums, target)}")

    