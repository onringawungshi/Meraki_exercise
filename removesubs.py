mainstr="the quick brown fox jumped over the lazy dog.the dog slept over the verandah"
mainstr.split(" ")
substr="on"
newstr=' '
i=0
while i<len(mainstr):
    if mainstr[i]=="over":
        newstr=newstr+substr
    else:
        newstr=newstr+mainstr[i]+''
    i+=1
print(newstr)