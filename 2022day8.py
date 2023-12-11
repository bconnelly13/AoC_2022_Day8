
with open("testData.txt", "r") as input:
    data = input.read()

rows = data.split()

# Test change

###################### Part 1 #######################
# def checkVisible(previous,curr):
#     for tree in previous:
#         if tree >= curr:
#             return False
#     return True

# visible = []

# ##### Checking Left to Right #####
# for i in range(len(rows)):
#     previous = ""
#     for j in range(len(rows[i])):
#         spot = [i,j]
#         curr = rows[i][j:j+1]
#         if spot not in visible:
#             if(checkVisible(previous,curr)):
#                 visible.append(spot)
#         previous += curr

# ##### Checking Right to Left #####
# for i in range(len(rows)):
#     row = rows[i]
#     previous = ""
#     for j in range(len(row)-1,-1,-1):
#         spot = [i,j]
#         curr = row[j:j+1]
#         if spot not in visible:
#             if(checkVisible(previous,curr)):
#                 visible.append(spot)
#         previous += curr



# ##### Checking Top to Bottom #####
# for j in range(len(rows[0])):
#     previous = ""
#     for i in range(len(rows)):
#         spot = [i,j]
#         curr = rows[i][j:j+1]
#         if spot not in visible:
#             if(checkVisible(previous,curr)):
#                 visible.append(spot)
#         previous += curr

# ##### Checking Bottom to Top #####
# for j in range(len(rows[0])):
#     previous = ""
#     for i in range(len(rows)-1,-1,-1):
#         spot = [i,j]
#         curr = rows[i][j:j+1]
#         if spot not in visible:
#             if(checkVisible(previous,curr)):
#                 visible.append(spot)
#         previous += curr

# print(f"Part 1 Answer: {len(visible)}")


######################### Part 2 ########################
def checkHorz(tree,spot,inc):
    count = 1
    vertPos = spot[0]
    horzPos = spot[1]
    row = rows[vertPos]
    tester = row[horzPos+(inc*count)]
    while tree > tester:
        count+=1
        tester = row[horzPos+(inc*count)]
    return count

def checkVert(tree,spot,inc):
    count = 1
    vertPos = spot[0]
    horzPos = spot[1]
    tester = rows[vertPos+(inc*count)][horzPos]
    while tree > tester:
        count += 1
        tester = rows[vertPos+(inc*count)][horzPos]
    return count

print(rows[0][-4])

for i in range(len(rows)):
    row = rows[i]
    for j in range(len(row)):
        tree = row[j:j+1]
        spot = [i,j]



