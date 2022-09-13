# numbers=[50,40,23,70,56,12,5,10,7,35,39]
# n=len(numbers)
# numbers.sort(reverse=True)
# index=0
# while index<n:
#     num=numbers[index]
#     if num<40:
#         print(num)
#     index=index+1

#find the length of the list?#

# places=["delhi","mumbai","kolkata","manipur","punjab","kerala"]
# p=len(places)-1
# index=p
# while index>=0:
#     print(places[index])
#     index-=1

#MAXIMUM#

# numbers=[60,30,20,80,100,90,10]
# numbers.sort()
# print(numbers[-1])

# numbers=[50,40,23,70,56,12,5,10,7]
# numbers.sort()
# print(numbers[-1])

# 
# find length of the list using whileloop?#

# mylist=[1,2,3,4,5,6,8,0.9]
# leng=len(mylist)
# i=0
# while i<leng:
#     print(leng)
#     i=i+leng

#print the numbers which are divisible by 2?#

# l=[6,8,1,4,9,2,0,5]
# i=0
# m=0
# while i<len(l):
#     if l[i]%2==0:
#         m=l[i]
#         print(m)
#     i=i+1

#print the list in reverse order?#
       
# mylist=[1,2,3,4]  
# leng=len(mylist)-1
# i=leng
# while i>=0:
#     print(mylist[i])  
#     i-=1 
 
# {

# list=[1,2,3,4]
# i=-1
# while i<0:
#     print(list[i])
#     i-=1
# }
#MAXIMUM#

# mylist=[89,90,12,34,101,55,60,20]
# i=1
# m=0
# while i<len(mylist):
#     if mylist[i]>m:
#         m=mylist[i]
#     i=i+1
# print(m)

#INPUT#

# mylist=[]
# i=0
# while i<4:
#     user=input("enter your items:")
#     mylist.append(user)
#     i+=1
# print(mylist)
    

#INPUT#
#MAXIMUM#

# lis=[]
# i=0
# while i<6:
#     n=int(input("enter number:"))
#     lis.append(n)
#     i=i+1
# j=0
# m=0
# while j<len(lis):
#     if lis[j]<m:
#         m=lis[j]
#     j+=1
# print(m)

#MINIMUM WITHOUT METHOD TAKING INPUT#
   
# lis=[]
# i=0
# while i<6:
#     n=int(input("enter number:"))
#     lis.append(n)
#     i=i+1
# j=0
# m=lis[0]
# while j<len(lis):
#     if lis[j]<=m:
#         m=lis[j]                                                                    
#     j=j+1
# print(m)
    

#PALINDROME#

# l=['n','i','t','i','n']
# i=0
# while i<len(l):
#     if l[0]==l[-1] and l[1]==l[-2]:
#         i=i+1
# print("palindrome")

# l=[1,2,3,4,5]
# l.extend([9,10])
# print(l)

#MINIMUM#

# l=[5,7,8,3]
# i=0
# m=0
# while i<len(l):
#     l.sort()
#     i+=1
# print(l[0])

#MINIMUM WITHOUT METHOD#

# l=[1,6,7,9,4]
# index=0
# min=l[0]
# while index<len(l):

#     if l[index]<min:
#         min=l[index]
#     index=index+1
# print(min)

#SECOND MAXIMUM WITHOUT METHOD TAKING INPUT#

#     intp=int(input("enter no."))
#     l.append(intp)
#     i=i+1
# j=0
# m=0
# while j<len(l):
#     if l[j]>m:
#         m=l[j]
#     j+=1
# print(m)


# l=[1,2,3,4]
# i=0
# m=0
# while i<len(l):
#     if l[i]>m:
#         m=l[i]
#     i+=1

string="onring"
i=0
while i<len(string):
    if i=="n":
        print(i,":","2")
    else:
        print(i,":","1")
    i+=1