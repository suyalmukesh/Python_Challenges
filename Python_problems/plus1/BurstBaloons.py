## Good Question and Tough (Medium)
def findMinArrowShots(points):

    if points is None : return 0 

    points.sort()
    prev = points[0]

    total = 1 

    for x1,x2 in points[1:]:

        if x1 > prev[1]:
            total += 1
            prev = [x1,x2]

        else:
           prev[1] = min(prev[1],x2)

    return total 







if __name__ == "__main__":
    inputs = [[[10,16],[2,8],[1,6],[7,12]],
              [[1,2],[3,4],[5,6],[7,8]],
              [[1,2],[2,3],[3,4],[4,5]],
              [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]]
    for points in inputs:
        print(findMinArrowShots(points))
