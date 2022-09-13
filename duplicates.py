# a=[1,2,3,4,1,2,3,4,5,6,7]
# c=[]
# i=0
# while i<len(a):
#     if a[i] not in c:
#         c.append(a[i])
#     i+=1
# print(c)

n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
m=[]
i=0
while i<len(n):
    if n[i] not in m:
        m.append(n[i])
    i+=1
print(m)