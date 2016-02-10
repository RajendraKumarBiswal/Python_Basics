##
##
##Suppose you have some string S having length N that is indexed from 0 to N−1.
##You also have some string R that is the reverse of string S.
##S is funny if the condition |Si−Si−1|=|Ri−Ri−1| is true for every i from 1 to N−1.
##Note: For some string str, stri denotes the ASCII value of the ith 0-indexed character
##in str. The absolute value of some integer, x, is written as |x|
##Sample Input
##2
##acxz
##bcxz
##Sample Output
##Funny
##Not Funny
##Explanation
##Test Case 0: S= "acxz" 
##|c−a|=2=|x−z| 
##|x−c|=21=|c−x| 
##|z−x|=2=|a−c| 
##We print Funny. 
##
##

t=int(raw_input().strip())
for i in range(t):
    s=raw_input().strip()
    print "Funny" if [abs(ord(s[i])-ord(s[i-1])) for i in range(1,len(s))] == [abs(ord(s[i])-ord(s[i-1])) for i in range(len(s)-1,0,-1)] else "Not Funny"
