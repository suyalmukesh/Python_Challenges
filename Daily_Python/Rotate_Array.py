def rotate(nums, k):
   
    n = len(nums)
    while k > n: k = k-n 
    
    temp = nums[n-k:n]

    for i in range(n-1,k-1,-1):
       nums[i] = nums[i-k]
    for i in range(len(temp)):
       nums[i] = temp[i]
    return nums       




if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    output =  [5,6,7,1,2,3,4]
    out = rotate(nums,k)
    if out == output:
       print("Correct")
    else:
       print(f"{out} is not correct output for {nums} for k = {k}")   


    nums = [-1,-100,3,99]
    k = 2
    output =  [3,99,-1,-100]
    out = rotate(nums,k)
    if out == output:
       print("Correct")
    else:
       print(f"{out} is not correct output for {nums} for k = {k}")  