def rotate1(nums, k):
    print("Brute Force")
    # Time limit Exceeded 
    while k >= 0:
         
        temp = nums[-1] 
        for i in range(len(nums)-1,-1,-1):
                nums[i] = nums[i-1]
        nums[0] = temp         
        k -= 1 
    return nums     

def rotate2(nums,k):
    print("Solution 2:")    
    result = []
    n = len(nums)
    result = [0]*n
    n = n-1
    while k > n :
         k = k - n
    
    for i in range(len(nums)):
        pos = i+k 
        if pos > n:
            pos = pos - n -1 
        result[i] = nums[pos]
                 
    return result              

def rotate3(nums,k):
    print("Solution 3 : ") 
    n = len(nums)
    result = [0]*n

    for i in range(n):
         
        pos = (i+k) % n
        result[i] = nums[pos]
    return result 


def rotate4(nums,k):

    print("O(1) space solution ") 
    k = k % len(nums)

    # reverse 
    left , right = 0 , len(nums) - 1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left , right = left + 1, right - 1
    print("REversed : ",nums)

    nums[0:k] = nums[0:k][::-1]
    nums[k:] = nums[k:][::-1]

    print(nums)
    return nums  



if __name__ == "__main__":

    nums = [1,2,3,4,5,6,7]
    k = 3
    print(rotate1(nums, k))
    nums = [1,2,3,4,5,6,7]
    print(rotate2(nums, k))
    nums = [1,2,3,4,5,6,7]
    print(rotate3(nums, k))
    nums = [1,2,3,4,5,6,7]
    print("Optimal",rotate4(nums, k))

    nums = [-1,-100,3,99]
    k = 2
    print(rotate1(nums, k))
    nums = [-1,-100,3,99]
    print(rotate2(nums, k))
    nums = [-1,-100,3,99]
    print(rotate3(nums, k))
    nums = [-1,-100,3,99]
    print("Optimal",rotate4(nums, k))
    
   