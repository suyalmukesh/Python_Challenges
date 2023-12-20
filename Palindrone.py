def isPalindrome(s):
    
    combined = ""
    for char in s:
        if char.isalpha() or char.isalnum():
           char = char.lower() 
           combined += char
    
    if len(combined) == 0:
        return True
    
    left = 0
    right = len(combined) - 1

    print(combined[left],combined[right])
    while left <= right:
        if combined[left] != combined[right]:
            return False
        else:
            left += 1
            right -= 1 
    return True
  
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
    print("-----------------------------------")
    s = "race a car"
    print(isPalindrome(s))
    print("-----------------------------------")
    s = " "
    print(isPalindrome(s))
    print("-----------------------------------")
    s = "0P"
    print(isPalindrome(s))
    print("-----------------------------------")