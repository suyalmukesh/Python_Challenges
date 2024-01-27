def minWindow(s,t):

    def remove(ch,temp):
        for i in range(len(temp)):
            if temp[i] == ch:
                del temp[i]
                return temp


    t_list = [x for x in t]
    temp = t_list
    output = {}
    print(t_list)
    for i in range(len(s)):
        temp = t_list         
        left = right = i
 

        if s[left] not in temp:
            continue 
        else:
            
            while right < len(s):
                if s[right] in temp:
                    temp = remove(s[right],temp)
                
                right = right + 1
                if len(temp) == 0:
                    if s[left:right] in output:
                        output[s[left:right]] = min(len(s[left:right]),output[s[left:right]])
                    else:
                        print(f"Length : {len(t_list)}")
                        if len(s[left:right]) >= len(t_list):
                            output[s[left:right]] = len(s[left:right])
                   
                    t_list = [x for x in t]
                    temp = t_list
              
                    right = len(s)   
    print(output) 
    min_value = len(s)
    for key,value in output.items():
        min_value = min(min_value,value)
    for key,value in output.items():
        if value == min_value:
            return key      
    return ""
    





if __name__ == "__main__": 
    
    inputs_s = ["ADOBECODEBANC","a","a","aaflslflsldkalskaaa"]
    inputs_t = ["ABC","a","aa","aaa"]
    expected = ["BANC","a","","aaa"]

    for i in range(len(inputs_s)):
        if i ==3:

            s = inputs_s[i]
            t = inputs_t[i]

            result = minWindow(s,t)
            if result == expected[i]:
                print(f"'{result}' is the Correct Answer")
            else:
                print(f"'{result}' is NOT the correct answer")    

