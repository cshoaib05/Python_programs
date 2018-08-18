class Employe:
    def __init__(self,Fname,Lname,Email,Salary):
        noE=0
        F=Fname
        L=Lname
        E=Email
        S=Salary
        noE=noE+1
    def raiseS(self,S):
        rpercent=10
        self.S=S+S*rpercent/100
        return S
        
Fname=(input("ENTER YOUR FIRST NAME"))
Lname=(input("ENTER LAST NAME"))
Email=(input("ENTER EMail"))
Salary=int(input("ENTER SALARY"))
o=Employe(Fname,Lname,Email,Salary)
print(o.raiseS(Salary))
