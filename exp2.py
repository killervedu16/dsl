marks=[]
n= int(input("Enter the number of students:"))
for i in range (0,n):
    enter= int(input("Enter your marks(if absent score=-1):"))
    marks.append(enter)
print(marks[:])

#average score of class
def avg():
    s=0
    for i in range (0,n):
        if marks[i] != -1:

            s = s + marks[i];
            print(s)
            avg = s/ n
    print (s)
    print("The average score of the class is: ",avg)

# highest and lowest score
def hlscore():
    high=marks[0]
    low=marks[0]

    for i in range(0,n):
        if marks[i]!= -1:
            if (marks[i]>=high):
                high= marks[i]
            elif(marks[i]<=low):
                low= marks[i]
    print("The highest score is = ",high)
    print("The lowest score = ",low)



# count number of students who were absent for the test
def count():
    count=0
    for i in range (0,n):
        if marks[i]==-1:
            count=count+1
    print("The number of students who were absent for the test= ",count)
    

def high_frequency():
    temp={}
    for element in marks:
        if element in temp:
            temp[element]+=1
        else:
            temp[element]=1
    print(temp)


print("FUNDAMENTAL OF DATA STRUCTURE TEST ANALYSIS")
print("1)Average Score of class.")
print("2)Highest and lowest score.")
print("3)Count of absent students.")
print("4)Display marks with highest frequency")
choice=int(input("Enter your choice:"))
if(choice==1):
    avg()
elif(choice==2):
    hlscore()
elif(choice==3):
    count()
elif(choice==4):
    high_frequency()
