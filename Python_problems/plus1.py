def plusOne(digits):
  
    ## Reverse the array 
    digits = digits[::-1]
    
    carry = 1 
    
    for i in range(len(digits)):
        sum = carry + digits[i]
        if sum > 9:
            sum = 0
            carry = 1 
            digits[i] = sum 

    print(digits)        




if __name__ == "__main__":

    inputs = [[1,2,3,4],[5,9],[9],[],[9,9,9,9],[9,8,9]]
    output = [[1,2,3,5],[6,0],[1,0],[],[1,0,0,0,0],[9,9,0]]

    count = 0 
    for i in range(len(inputs)):
        count += 1
        out = plusOne(inputs[i])
        if out == output[i] : 
            print(f"Case {count} :: Correct ")
        else: 
            print(f"Case {count} :: Failed , {out}") 



       