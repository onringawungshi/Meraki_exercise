l = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
c=0
x=0
y=0
while i<len(l):
    if l[i]>10000000:
        c=c+1
    elif l[i]>100000:
        x=x+1
    else:
        y+=1
    i+=1
print("There are",c,"crorepati in the list")
print("there are",x,"lakhpati in the list")
print("There are",y,"dilwale in the list")



# l = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# i=0
# while i<len(l):
#     if l[i]>=10000000:
#         print(l[i],"=crorepati")
#     elif l[i]>100000:
#         print(l[i],"=lakhpati")
#     else:
#         print(l[i],"=dilwale")
#     i+=1
 