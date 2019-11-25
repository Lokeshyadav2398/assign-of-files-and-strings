tlist=["Hello world","Bye World","I am in this WoRld"]
count=0
for i in range(len(tlist)):
	word=tlist[i]
	word.casefold()
	sub="world"
	count=count+1
print("world :%d" % count)
	