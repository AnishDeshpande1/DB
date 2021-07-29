import os
l = []
namefolder = "webcrawler"
for file in os.listdir(namefolder):
    if file[:4] == "part":
        f = open(os.path.join(namefolder, file), "r")
        l += f.readlines()
l = sorted(l)
f = open("output.txt", "a")
for x in l:
    f.write(x)
f.close()