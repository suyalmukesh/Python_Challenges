def findSubstring2(s, words):
    n = len(words)
    m = len(words[0])
    wind_len = n * m 

    out = []  
    left = 0
    
    for i in range(wind_len,len(s)+1):
        word_cp = words 
        window = s[left:i]
       #print(window)
    
        j = 0 
    
        while j < n:
            #print(j,words[j])
            if words[j] in window:
                j+=1
                
            else:
                break
        if j == n :
            out.append(left)
        left += 1     

    return out     


def findSubstring(s, words):

    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
   
    n , m = len(words) , len(words[0])
    win_size = n*m

    left = 0 
    right = win_size - 1
    out = []
    while right < len(s):
        temp = s[left:right+1]
       
        temp_dict = {}

        for i in range(0,len(temp),m):
            pick = temp[i:i+m]
          
            if pick in temp_dict:
                   temp_dict[pick] += 1
            else:
                temp_dict[pick] = 1 
       

        if temp_dict == word_dict:
            out.append(left)
       
         
        left += 1 
        right += 1    

    return out
    
      

    
if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    print(findSubstring(s,words))
    print("_________________________________")
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    print(findSubstring(s,words))
    print("_________________________________")
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    print(findSubstring(s,words))
    print("_________________________________")

