question=["How many continents are there?",
"What is the capital of India?",
"Python 3 was invented which year?"]


options_list = [["Four", "Nine", "Seven", "Eight"],
                ["Chandigarh", "Bhopal","Chennai", "Delhi"],
                ["2008","2004","2003","2010"]]
solution_list = [3, 4, 1]
fifty_op=[["Four","Seven"],
          ["Chennai","Delhi"],
          ["2008","2010"]]
fifty_ans=[2,2,1]
def fifty_fifty(i):
    x=0
    if x==0:
        z=0
        while z<len(fifty_op[i]):
            print(z+1,fifty_op[i][z])
            z+=1
        usr=int(input("enter your ans:"))
        x+=1
        if usr==fifty_ans[i]:
            return "True"
        else:
            return "False"
    else:
        print("You already used 5050 lifeline")
        # return "y"
def options(i):
    j=0
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j+=1
    user=int(input("enter answer:"))
    if user==solution_list[i]:
        return "correct"
    if user==5050:
        return fifty_fifty(i)
    else:
        return "incorrect"          
def question_list():
    i=0
    while i<len(question):
        print(i+1,question[i])
        x=options(i)
        if x=="correct":
            print("correct")
            print("Congratulation!!")
        else:
            print("Not Correct")
            print("Game Over!!")
            break
        i+=1
question_list()

# a=[[12],[13,4,6],[1],[2,[3],4,5]]
# print(a[3][1][0],end=",")
# print(a[3][3],end=",")
# print(a[1][1],end=",")
# print(a[0][0],end="")