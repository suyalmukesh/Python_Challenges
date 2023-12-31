def evalRPN(tokens):

    stack = []
    symbols = ["+","-","/","*"]

    for char in tokens:
        if char not in symbols:
            char = int(char)   
            stack.append(char)
            
        elif char in symbols:
            
            a = stack.pop()
            b = stack.pop()

            a , b = int(a) , int(b) 
            
            if char == '+':
                result = a + b

            elif char == '-':
                result = b - a

            elif char == '*':
                result = a*b

            elif char == '/':
                result = b/a

            stack.append(result)
            
        else:
            print(f"Stack has error : {stack}")   
    
    res = stack.pop() 
    
    return res        
        

if __name__ == "__main__":

    tokens = ["2","1","+","3","*"]
    print(evalRPN(tokens))
    print("---------------------------------------")

    tokens = ["4","13","5","/","+"]
    print(evalRPN(tokens))
    print("---------------------------------------")

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))
    print("---------------------------------------")