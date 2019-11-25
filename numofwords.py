count=0
fd=open("words.txt","r")
for line in fd:
    words=line.split()
    count=count+len(words)
print("number of words:",count)
fd.close()