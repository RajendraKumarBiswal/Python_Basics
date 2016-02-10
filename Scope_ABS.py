### All About SCope ###
##
##Input Format
##The first line contains a positive integer, N, denoting the size of array elements.
##The second line contains N space-separated positive integers describing elements.
##Constraints 
##1≤N≤10 
##1≤elements[i]≤100, where 0≤i≤N−1 
##Output Format
##Print the maximum absolute difference between any two integers in elements.
##Sample Input
##3
##1 2 5
##Sample Output
##4
##Explanation
##|1-2|=1  
##|1-5|=4  
##|2-5|=3  
##We print the maximum of these absolute differences, which is 4.

class Difference:
    def __init__(self, a):
        self.__elements = a
    # Add your code here
    def computeDifference(self):
        self.maximumDifference=0
        for i in range(0,len(self.__elements)):
            for j in range(0,len(self.__elements)):
                if i!=j:
                    tmp = abs(self.__elements[i] - self.__elements[j])
                    self.maximumDifference = tmp if self.maximumDifference < tmp else self.maximumDifference

    # End of Difference class

N = int(raw_input().strip())
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference        
