def merge(intervals):

    intervals.sort()
    output = []
    first = intervals[0]
    left = first[0]
    right = first[1]

    count = 1
    for i in range(1,len(intervals)):
        
        if intervals[i][0] <= first[1]:
            right = max(intervals[i][1],first[1])
            left = min(intervals[i][0],first[0]) 
                    
        else:
            output.append([left,right])
            first = intervals[i]
            left = first[0]
            right = first[1]
        
    
    output.append([left,right])    
   
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