def longestCommonPrefix1(strs):
    result = ""
    strs.sort()
    left , right = 0 , len(strs) - 1
    for i in range(len(strs[0])):
        if strs[left][i] != strs[right][i]:
            return result     
        else:
            result += strs[left][i] 

    return result  
## --------------------------------------------------
def longestCommonPrefix2(strs):
    result = strs[0]
    n = len(result)

    for i in range(1,len(strs)):
        while strs[i].find(result) != 0:
            result = result[:n-1]
            n = n - 1

            if not result:
                return -1
    return result         

## ------------------------------------------------
def longestCommonPrefix3(strs):

    result = ""

    for i in range(len(strs[0])):

        for word in strs:
            if i == len(word) or word[i] != strs[0][i]:
                return result 
        result += word[i]
    
    return result 
## ---------------------------------------------------

if __name__ == "__main__":
    inputs = [["flower","flow","flight"],["dog","racecar","car"]]
    
    for strs in inputs:
        print("Method 1 ",longestCommonPrefix1(strs))
        print("------------------------------------------------") 
        print("Method 2 ",longestCommonPrefix2(strs))
        print("------------------------------------------------") 
        print("Method 3 ",longestCommonPrefix3(strs))
        print("------------------------------------------------") 