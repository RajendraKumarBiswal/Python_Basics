##You are given a pointer root pointing to the root of a binary tree.
##You need to print the level order traversal of this tree.
##In level order traversal, we visit the nodes level by level from left to right. 
## For example: 
##         3
##       /   \
##      5     2
##     / \    /
##    1   4  6
##For the above tree, the level order traversal is 3 -> 5 -> 2 -> 1 -> 4 -> 6.
##HINT: A queue could be helpful. 
##Sample Input
##6
##3
##5
##4
##7
##2
##1
##Sample Output
##3 2 5 1 4 7 
##Explanation
##Level 1:        3
##              /   \
##Level 2:     2     5
##            /     /\
##Level 3:   1     4  7 
##We need to print the nodes level by level.
##We process each level from left to right. 
##Level Order Traversal: 3 -> 2 -> 5 -> 1 -> 4 -> 7


import sys
class Node:
    def __init__(self,data):
        self.right = self.left = None; self.data = data;

class Solution:
    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left,data)
                root.left = cur
            else:
                cur = self.insert(root.right,data)
                root.right = cur
        return root

    def levelOrder(self,root):
        if root == None: return
        self.tmp = [root]; _out = "";
        while self.tmp:
            l = list();
            for n in self.tmp:
                _out += str(n.data) + " ";
                if n.left: l.append(n.left);
                if n.right: l.append(n.right);
            self.tmp = l;
        print _out[:len(_out)-1]


T = int(raw_input())
myTree = Solution()
root = None
for i in range(T):
    data = int(raw_input())
    root = myTree.insert(root,data)
myTree.levelOrder(root)
