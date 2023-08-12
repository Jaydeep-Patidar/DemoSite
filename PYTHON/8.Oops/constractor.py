class student:
    "to get student information"
    schoolname="cps"
    id=12
    name="jaydeep"
    email="jaydeeppatidarj@gmail.com"
    
    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email
        print("value set....")
    
    def displaystudentdata(self):
        print("id:",self.id)
        print("name:",self.name)
        print("email:",self.email)
        print()
    
ob=student(1,"patidar","patidar@gmail.com")
ob.displaystudentdata()
    
ob2=student(2,"sonika","sonikapatidarsp@gmail.com")
ob2.displaystudentdata()

print(student.__doc__)
print(student.id)
print(student.name)
print(student.email)
print()
