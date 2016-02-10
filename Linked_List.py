## Linked List ##
##Input Format
##First line contains T, the number of testcases.
##Each test case contains an integer to be inserted at tail of linked list.
##Output Format
##Output the data in each node separated by space.
##Sample Input
##4
##2
##3
##4
##1
##Sample Output
##2 3 4 1
##Explanation
##T=4 
##Initially head is null and 2 is inserted. 3,4,1 are inserted at the tail of
##linked list hence the linked list becomes 2 3 4 1


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next
    def insert(self,head,data):
        obj=Node(self)
        obj.data = data
        #self.cnt_node = 1 if head == None else self.cnt_node+=1
        if head != None: self.cur_node.next = obj
        self.cur_node = obj
        #if head !=None & self.cnt_node == 2: head.next=obj
        #else: obj.next=head
        return obj if head == None else head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);

