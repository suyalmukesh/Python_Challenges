def findMinArrowShots(points):


    pass


if __name__ == "__main__":

    inputs = [[[10,16],[2,8],[1,6],[7,12]],[[1,2],[3,4],[5,6],[7,8]],[[1,2],[2,3],[3,4],[4,5]]]
    answers = [2,4,2]

    for i in range(len(inputs)):
        print(f"Case : {i+1}")
        result = findMinArrowShots(inputs[i])
        if result == answers[i]:
            print(f"[CORRECT] : Miniumn Arrow required = {result}")
        else:
            print(f"result {result} is NOT correct")
