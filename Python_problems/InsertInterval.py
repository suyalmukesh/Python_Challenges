def insert(intervals, newInterval):

    output = [] 
    for i in range(len(intervals)):

        if newInterval[1] < intervals[i][0]:
            output.append(newInterval)
            return output + intervals[i:]
        
        elif newInterval[0] > intervals[i][1]:
            output.append(intervals[i])
        
        else:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])             

    output.append(newInterval) 
    return output
       
        
              



if __name__ == "__main__":

    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    Output = [[1,5],[6,9]]
    result = insert(intervals, newInterval)
    if result == Output:
        print("Correct")
    else: 
        print(f"{result} not correct")    
    
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    Output = [[1,2],[3,10],[12,16]]
    result = insert(intervals, newInterval)
    if result == Output:
        print("Correct")
    else: 
        print(f"{result} not correct")    