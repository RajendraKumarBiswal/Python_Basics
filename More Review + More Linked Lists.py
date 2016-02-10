##  More Review + More Linked Lists  ##

##Given a pointer to the head node of a linked list whose data elements are in non-decreasing order, you must delete any duplicate nodes and print the updated list.
##Code handling I/O is provided in the editor. Complete the removeDuplicates(Node) function. 
##Note: The head pointer may be null, indicating that the list is empty. Be sure to reset your next pointer when performing deletions to avoid breaking the list.
##Input Format
##The first line contains N, the number of nodes to be inserted. 
##The N subsequent lines each contain an integer describing the data for a node being inserted at the list's tail;
##the lines of data will always be in non-decreasing order.
##Output Format
##Print the data for your list of ascending nodes as a single line of space-separated integers.
##Sample Input
##6
##1
##2
##2
##3
##3
##4
##Sample Output
##1 2 3 4 
##Explanation
##N = 6, and our non-decreasing list is {1,2,2,3,3,4}. The data values 2 and 3 each have a duplicate,
##so we remove the two duplicate nodes and print our updated (ascending) list


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:   
    def insert(self,head,data):
        p = Node(data)        
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head
    
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next

    def removeDuplicates(self,head): ########
        if head==None or head.next ==None: return head
        tmp = head;
        while tmp.next!=None:
            if tmp.data==tmp.next.data: tmp.next=tmp.next.next;
            else: tmp=tmp.next;
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)   
head=mylist.removeDuplicates(head)
mylist.display(head);
