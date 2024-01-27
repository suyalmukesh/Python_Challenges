def shortestDistance(wordsDict, word1, word2):
    
    n = len(wordsDict)
    l1 , l2 = n,n
    for i,key in enumerate(wordsDict):

        if l1 >= 0 and l2>=0 :

            min_value = min(min_value,)









if __name__ == "__main__":

    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    output =  3
    result = shortestDistance(wordsDict, word1, word2)
    if result == output:
        print("Correct")
    else:
        print(f"{result} is NOT correct ")    


    wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "coding"
    output= 1
    result = shortestDistance(wordsDict, word1, word2)
    if result == output:
        print("Correct")
    else:
        print(f"{result} is NOT correct ")   

    wordsDict = ["a","a","b","b"]
    word1 = "a"
    word2 = "b"
    output= 1
    result = shortestDistance(wordsDict, word1, word2)
    if result == output:
        print("Correct")
    else:
        print(f"{result} is NOT correct ") 

    wordsDict = ["a","c","b","b","a"]
    word1 = "a"
    word2 = "b"
    output= 1
    result = shortestDistance(wordsDict, word1, word2)
    if result == output:
        print("Correct")
    else:
        print(f"{result} is NOT correct ")           
