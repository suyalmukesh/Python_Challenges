def hIndex(citations):
    
    citations.sort()

    N = len(citations)
    i = 0
    while i < N and N - i > citations[i]: 
        i += 1
    return N - i     
    # Refer for understanding :: https://www.youtube.com/watch?v=QWrGZ9Eq2I8&t=17s

if __name__ == "__main__":

    inputs = [[3,0,6,1,5],[3,0,6,7,8,5],[1,3,1],[100],[1,1,2,2,2,2,20],[1,2,3,3,3]]
    for citations in inputs:
        print(f"H-Index for {citations} :: ",hIndex(citations))

## Understanding H-Index is quite complex (at least for me ) . Good question , found tricky         