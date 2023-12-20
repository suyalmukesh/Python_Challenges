def intToRoman(num):
    
    # 1. Store roman numbers in decending order in list 
    # 2. Now compare the given numbers with the list one by one 
    ##   if num < given num pass
    ##   if num > given num , add corresponding literal and substract substract num from given_num     

    roman_string = ""

    roman_num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

    i = 0 
    
    while num > 0 and i < len(roman_num):   
     
        if num >= roman_num[i]:
            
            roman_string += roman_sym[i]
            
            num = num - roman_num[i]
            
        else:
            i += 1
           
    return roman_string        





if __name__ == "__main__":
    inputs = [3,58,1994,10,20]
    
    for num in inputs:
        print(intToRoman(num))
        print("------------------------------")
