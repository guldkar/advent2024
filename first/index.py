import csv
import operator

reader = csv.reader(open("./input.txt"))

distances = []
left = []
right= []
# def splitAndConvertLists(row):


for row in reader:
    row = row[0].split("   ")
    row[0], row[1] = [int(num) for num in row[0]], [int(num) for num in row[1]]
    left.extend(row[0])
    right.extend(row[1])
    row[0].sort()
    row[1].sort()
    for i in range(len(row[0])):
        distances.append(abs(row[0][i]-row[1][i])) 
    # res = map(lambda a,b: abs(a-b), row[0], row[1])
    # myList =list(res)
    # distances.extend(myList)
    
    # distances.append(res)
print(sum(distances))

