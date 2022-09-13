lists=[23,45,65,87,90,88]
i=0
m=0
while i<len(lists):
    if lists[i]>m:
        m=lists[i]
    i+=1
print(m)