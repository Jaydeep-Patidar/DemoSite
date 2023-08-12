class A:
    def Adata(self):
        print("method of A")
    def getdata(self):
        print("in A")
class B:
    def Bdata(self):
        print("method of B")
    def getdata(self):
        print("in B")
class C(B,A):
    def Cdata(self):
        print("method of C")
        
          
ob=C()
ob.getdata()


class student:
    id=0
    name=""
    def getdata(self):
        self.id=input('enter the id:')
        self.name=input('enter the name:')
        
class exam(student):
    sub1=0
    sub2=0
    def getmarks(self):
        self.sub1=int(input("enter sub1 marks:"))
        self.sub2=int(input("enter sub2 marks:"))
        self.sub3=int(input("enter sub3 marks:"))
        self.sub4=int(input("enter sub4 marks:"))
        self.sub5=int(input("enter sub5 marks:"))
        self.sub6=int(input("enter sub6 marks:"))
        
    
    def result(self):
        print("\nstudent id:",self.id)
        print("student name:",self.name)
        print("sub1:",self.sub1)
        print("sub2:",self.sub2)
        print("sub3:",self.sub3)
        print("sub4:",self.sub4)
        print("sub5:",self.sub5)
        print("sub6:",self.sub6)
        total=self.sub1+self.sub2+self.sub3+self.sub4+self.sub5+self.sub6
        print("total:",total)
        per=total/6
        print("result:",per)
        
        

ex=exam()
ex.getdata() 
ex.getmarks()
ex.result()