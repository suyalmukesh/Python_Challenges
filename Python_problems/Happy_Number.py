def isHappy(n):
    
    used = set()

    while True: # infinite loop 
        
        sum = 0 

        while n != 0 :
            sum = sum + pow(n%10 , 2)
            n = n // 10

        if sum == 1: return True 

        if sum in used:
            return False 
        else:
            used.add(sum)
            n = sum           


if __name__ == "__main__":
    inputs = [19,2]
    for n in inputs:
        print(isHappy(n))
        print("\n\n") 