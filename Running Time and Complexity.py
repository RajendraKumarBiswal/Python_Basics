##In this challenge, you will determine if a given number X is prime or not.
##A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
##You will be given N numbers and for each, you will print out "Prime" if the number is prime
##or "Not prime" if the number is not prime. 
##
##If this is too easy, create a method that decides if X is prime or not in O(√X) time.
##Think modulos and square root! If you are having trouble,
##try creating an O(X) time algorithm and see whether it solves the problem or not.
##
##To review Big-O Notation, remember...
##•Big-O "is used in Computer Science to describe the performance or complexity of an algorithm."
##•Big-O "specifically describes the worst-case scenario, and can be used to describe the execution time required or the space used (e.g. in memory or on disk) by an algorithm."
##
##Sample Input
##3
##12
##5
##7
##Sample Output
##Not prime
##Prime
##Prime


import math
def isPrime(n):
    flg=True
    #for i in range(2, n): ## O(x)
    for i in range(2, int(math.sqrt(n))+1): ## O(√X)
        if not (n%i):
            flg=False; break;
    print "Prime" if flg==True else "Not prime"
    return

T=int(raw_input().strip())
for i in range(T):
    n = int(raw_input().strip())
    if n < 2: print "Not prime";
    elif n==2:  print "Prime"
    else : isPrime(n);
