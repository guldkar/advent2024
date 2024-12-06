exampleData = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def checkAscension(report):
    for i in range(len(report)-1):
        diff = report[i+1] -report[i]
        if(  diff < 1 or diff > 3 ):
            return False

stringRows = 