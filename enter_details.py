rc=int(input("Enter the number of students: "))
for i in range(0,rc):
     print("\nEnter student ",i+1," Id: ",end="")
     id=str(input())
     print("Enter student ",i+1," name: ",end="")
     name=str(input())
     print("Enter student ",i+1," address: ",end="")
     address=str(input())
     print("Enter student ",i+1," marks: ",end="")
     marks=int(input())
     print("\nStudent",i+1,"details:")
     print("Student",i+1,"Id: ",id)
     print("Student",i+1,"name: ",name)
     print("Student",i+1,"address: ",address)
     print("Student",i+1,"marks: ",marks,"\n")