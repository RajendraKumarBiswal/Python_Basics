## Recursion!  - GCD --- ##
##It's in the standard library.
##
##>>> from fractions import gcd
##>>> gcd(20,8)
##4
##
##Source from the inspect module:
##>>> print inspect.getsource(gcd)
##def gcd(a, b):
##    """Calculate the Greatest Common Divisor of a and b.
##
##    Unless b==0, the result will have the same sign as b (so that when
##    b is divided by it, the result comes out positive).
##    """
##    while b:
##        a, b = b, a%b
##    return a

def find_gcd(a,b):
   #write base condition
    return a if (a==0 or b==0 or a==b) else find_gcd(b,a%b)
#Take input
#from fractions import gcd
t=raw_input().strip().split(' ')
gcd=find_gcd(int(t[0]),int(t[1]))
print gcd
    

def find_gcd(a,b):
   #write base condition
    return gcd(a,b)
#Take input
from fractions import gcd
t=raw_input().strip().split(' ')
gcd=find_gcd(int(t[0]),int(t[1]))
print gcd


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

###  This version of code utilizes Euclid's Algorithm for finding GCD.
def gcdIter(a, b):
    if b == 0:
        return a
    else:
        return gcdIter(b, a % b)
def gcd(m,n):
    return n if (m-n) == 0 else gcd(abs(m-n), min(m, n))
