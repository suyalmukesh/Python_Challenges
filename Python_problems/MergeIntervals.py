def merge(intervals):

    output = [] 
    intervals.sort()
    left = intervals[0]
    for i in range(1,len(intervals)):

        right = intervals[i]
        if right[0] <= left[1]:
            left[0] = min(left[0],right[0])
            left[1] = max(left[1],right[1])
        else:
            output.append(left)
            left = intervals[i]
    output.append(left)                
   
    return output

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output =  [[1,6],[8,10],[15,18]]
    #Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
    if merge(intervals) == Output:
        print(f"Output : {Output} : Correct")
    else: print(f"Output : Not Correct")    

    intervals = [[1,4],[4,5]]
    Output =  [[1,5]]
    if merge(intervals) == Output:
        print(f"Output : {Output} : Correct")
    else: print(f"Output : Not Correct")    

   
    intervals = [[1,3]]
    Output =  [[1,3]]
    if merge(intervals) == Output:
        print(f"Output : {Output} : Correct")
    else: print(f"Output : Not Correct")    



    intervals = [[1,4],[0,4]]
    Output =  [[0,4]]
    if merge(intervals) == Output:
        print(f"Output : {Output} : Correct")
    else: print(f"Output : Not Correct")    



    intervals = [[1,4],[0,1]]
    Output =  [[0,4]]
    if merge(intervals) == Output:
        print(f"Output : {Output} : Correct")
    else: print(f"Output : Not Correct")    

    
    intervals = [[1,4],[0,0]]
    Output =  [[0,0],[1,4]]
    if merge(intervals) == Output:
        print(f"Output : {Output} : Correct")
    else: print(f"Output {merge(intervals)} : Not Correct") 

    intervals = [[1,4],[0,2],[3,5]]
    Output =  [[0,5]]
    if merge(intervals) == Output:
        print(f"Output : {Output} : Correct")
    else: print(f"Output {merge(intervals)} : Not Correct") 