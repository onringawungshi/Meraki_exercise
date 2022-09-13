a=[1,2,"c","a",3.2,5.0]
i=0
b,c,d=[],[],[]
while i<len(a):
    if type(a[i])==str:
        b.append(a[i])
    elif type(a[i])==float:
        c.append(a[i])
    elif type(a[i])==int:
        d.append(a[i])
    i+=1
print(b[0])
print(c[0])
print(d[0])