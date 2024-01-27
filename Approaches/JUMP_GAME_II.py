def jump1(nums):  # Brute Force 
    pass

def jump2(nums):  # Recursion 
    pass

def jump3(nums):  # Dunamic Programming 
    pass

def jump4(nums):  # Greedy Approach
    
    totaljumps = 0 
    destination = len(nums) - 1
    coverage = 0 
    lastJumpIndex = 0 

    if len(nums) == 1 : return 0 

    for i in range(len(nums)):

        coverage = max(coverage,i+nums[i])

        if i == lastJumpIndex:
            lastJumpIndex = coverage 
            totaljumps += 1

        if coverage == destination:
            return totaljumps

    return totaljumps     

if __name__ == "__main__":
 
    Inputs =  [[2,3,1,1,4],[2,3,0,1,4]]

    for nums in Inputs:
        print(f"Brute Force : {jump1(nums)}")
        print(f"Recursion : {jump2(nums)}")
        print(f"Dynamic Programming : {jump3(nums)}") 
        print(f"Greedy Approach : {jump4(nums)}")        