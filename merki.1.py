n=[50,40,23,70,56,12,5,10,7]
i=0
j=0
while i<len(n):
    if n[i]<40 and n[i]>20:
        j=j+1
        print(n[i])
    i+=1
print(j)