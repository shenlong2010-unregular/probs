link1 = "https://www.youtube.com/watch?v=kbxkq_w51PM"
link2 = "https://youtu.be/KMBBjzp5hdc"

# print(link.find("="))
# print(link[32:-1])
# print(link2.find('/', 15, -1))
def youtubeLinkFinder(link):
    vID = ""
    for i in link:
        # long version
        if ".com" in link and i == "=":
            vID += link[link.find(i)+1:]
            break
        # short version
        if ".be" in link and i == "/":
            vID += link[link.find(i, 15, -1)+1:]
            break
    return vID

print(youtubeLinkFinder(link1))
print(youtubeLinkFinder(link2))
