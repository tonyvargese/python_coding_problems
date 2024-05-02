class student:
    def __init__(t,name,age,dept):
        t.name=name
        t.age=age
        t.dept=dept
    def display(t):
        print(f"name:{t.name} age:{t.age} dept:{t.dept}")
    def sub(t,sub):
        print(f"examination for {sub}")

name=input("enter the name ")
age=int(input("enter the age: "))
dept=input("enter the dept: ")
sub=input("enter the subject: ")
student1=student(name,age,dept )

student1.display()
student1.sub(sub)
        