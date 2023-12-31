def isValidSudoku(board):
    pass

def check_col(board):
    n = 9 
    
    for i in range(n):
        visited = []
        for j in range(n):
            if board[i][j] in visited:
                return False 
            else:
                visited.append(board[i][j])
    return True 

def check_row(board):
    n = 9 

    for i in range(n):
        visited = []
        for j in range(n):
            if board[j][i] in visited:
                return False 
            else:
                visited.append(board[j][i])
    return True 


def check_3x3(board):

    row_group  = 0 

    out = []

    
    k = 3 
    while row_group < 3:
        k = 0 
        while k < 3:
            for i in range(row_group):
                for j in range(row_group,k):
                    out.append(board[i][j])
            
    print(out)        
           
       







if __name__ == "__main__":

    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    #print(isValidSudoku(board))
    print(check_3x3(board))
    print("-----------------------------------------------------")

    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    #print(isValidSudoku(board))
    print(check_3x3(board))
    print("-----------------------------------------------------")