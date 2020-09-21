myname = "Z"
agents = 5
nameL = "J M O S"

def newLicense(myname, agents, nameList):
    lst = nameList
    lst.append(myname)
    lst.sort()
    print(int((lst.index(myname)) // agents)* 20+20)

newLicense(myname, agents, nameL.split())

# arr = [(5, 8, 0), (2, 4)]
# sum = []
# for x, *y in arr:
#     sum += y
# print(sum)