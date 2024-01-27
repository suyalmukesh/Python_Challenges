def simplifyPath(path):

   # Test = "/a/./b/../../c/"

    root = "/"
    stack = []
    path_list = path.split('/')

    for char in path_list:
        if char == '.':
            pass
        elif char == '..':
            if len(stack) >= 1:
                stack.pop()
        elif len(char) > 0:
            stack.append(char)
   
    out = '/'.join(stack)   
    
    output = root+out
    return output



if __name__ == "__main__":

    path = "/home/"
    print(f"{path} simplified to {simplifyPath(path)}")

    path = "/../"
    print(f"{path} simplified to {simplifyPath(path)}")

    path = "/home//foo/"
    print(f"{path} simplified to {simplifyPath(path)}")

    path = "/a/./b/../../c/"
    print(f"{path} simplified to {simplifyPath(path)}")
    


"""

Notes : 

/abc/..   =>  It means first it will go abc directory . Then '..' means it will go out side of abc ==> /


/abc/.  => stay where you are ==> /abc 


/../abc//./def/    => Now after encountering first '..' we can't go beyond root directory so we will ignore this . 
                     
                   => /abc/def







"""