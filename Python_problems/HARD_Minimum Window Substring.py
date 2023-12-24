def minWindow(s,t):
      
   if len(t) > len(s): return ""
   n = len(s)
   t_dict = {}
   for char in t:
       if char in t_dict:
           t_dict[char] += 1
       else:
           t_dict[char] = 1

   required_count = len(t)

   i , j = 0,0
   
   window_size = float("inf")
   start_i = 0 

   while j < n:  
        ch = s[j]
        if t_dict[ch] > 0:
            required_count -= 1
        t    
               

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s,t))
    print("--------------------------") 

    s = "a"
    t = "a"
    print(minWindow(s,t))
    print("--------------------------") 


    s = "a"
    t = "aa"
    print(minWindow(s,t))
    print("--------------------------") 
