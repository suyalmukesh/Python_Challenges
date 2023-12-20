def strStr(haystack, needle):
   
   if haystack == needle : return 0 

   if len(needle) > len(haystack) : return -1 

   size_of_needle = len(needle)

   for i in range(len(haystack)-size_of_needle + 1):
      
      pick = haystack[i:i+size_of_needle]
      print(f"i = {i} :: pick = {pick}")
      if pick == needle:
         return i 
      
   return -1    



if __name__ == "__main__":

   haystack = "sadbutsad" 
   needle = "sad"
   print(strStr(haystack, needle))

   haystack = "leetcode"
   needle = "leeto"
   print(strStr(haystack, needle))

   haystack = "abc"
   needle = "c"
   print(strStr(haystack, needle))