class Student:
    def __init__(self,firstName,lastName,phone):
        self.firstName=firstName
        self.lastName=lastName
        self.phone=phone
    def display(self):
        print ("First Name:",self.firstName)
        print ("Last Name:",self.lastName)
        print ("Phone:",self.phone)

##class Grade(Student):       
###  Need to  update this class ### -- Alraedy Updated wth constru & fun
class Grade(Student):
    def __init__(self,firstName,lastName,phone,score):
        self.score =score
        self.firstName=firstName
        self.lastName=lastName
        self.phone=phone
    def calculate(self):
        if self.score < 40: return 'D'
        elif 40 <= self.score < 60: return 'B'
        elif 60 <= self.score < 75: return 'A'
        elif 75 <= self.score < 90: return 'E'
        else: return 'O'

firstName=input().strip()
lastName=input().strip()
phone=int(input())
score=int(input())
stu=Grade(firstName,lastName,phone,score)
stu.display()
print ("Grade:",stu.calculate())

##------ Input  ----------  ##
##Heraldo
##Memelli
##8135627
##90

## ------ Output  -------- ##
##First Name: Heraldo
##Last Name: Memelli
##Phone: 8135627
##Grade: O
