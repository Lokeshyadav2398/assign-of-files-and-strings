c1=0
c2=0
fd=open("count.txt","r")
for line in fd:
    sub = "EDFFX2AD"
    c1=c1+line.count(sub)
fd.close()
fd=open("count.txt","r")
for line in fd:
    sub = "DFFQXLAD"
    c2=c2+line.count(sub)
fd.close()

count=c1+c2
print(count)