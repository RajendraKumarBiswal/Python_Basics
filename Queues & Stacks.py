 ##   Queues & Stacks    ##

##Sample Input
##racecar
##Sample Output
##The word, racecar, is a palindrome.

import sys

class Palindrome:
    #Write your code here
    def __init__(self):
        self.l1 = {};  self.l2 = [];
        return
    def pushCharacter(self,x):
        self.l1[len(self.l1)] = x
        return
    def enqueueCharacter(self,x):
        self.l2.append(x)
        return
    def popCharacter(self):
        return self.l1.pop(len(self.l1)-1)
    def dequeueCharacter(self):
        return self.l2.pop(0)


# read the string s
s=raw_input()
#Create the Palindrome class object
p=Palindrome()   

l=len(s)
# push all the characters of string s to stack
for i in range(l):
    p.pushCharacter(s[i])
#enqueue all the characters of string s to queue
for i in range(l):
    p.enqueueCharacter(s[i])
f=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l):
    if p.popCharacter()!=p.dequeueCharacter():
        f=False
        break
#finally print whether string s is palindrome or not.
if f:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")    
    



