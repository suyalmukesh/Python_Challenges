def convert(s, numRows):
   
   if numRows == 1 : return s 

   ind = -1 
   i = 0 

   ans = [''] * numRows
   zigzag_output  = ""

   for char in s:
       ans[i]+=(char) 
       if (i == 0) or (i == numRows -1):
           ind = -1 * ind
       if ind == 1:
           i += 1
       else:
           i -= 1 

   
   zigzag_output = ''.join(ans)
   
   return zigzag_output
                   



if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numrows = 3
    output =  "PAHNAPLSIIGYIR"
    if convert(s,numrows) == output:
        print(f"{s} -> {output} :: PASSED")

    s = "PAYPALISHIRING"
    numrows = 4
    output =  "PINALSIGYAHRPI"
    if convert(s,numrows) == output:
        print(f"{s} -> {output} :: PASSED")
