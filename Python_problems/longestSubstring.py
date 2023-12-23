def lengthOfLongestSubstring(s):
    charSet = set()
    
    left = 0

    result = 0 

    for right in range(len(s)):
        while  s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        result = max(result,right - left + 1)
        
    return result     
  





if __name__ == "__main__":
    inputs = ["abcabcbb","bbbbb","pwwkew","dvdf"]
    for s in inputs:
        print(lengthOfLongestSubstring(s))
        print("---------------------------------")

