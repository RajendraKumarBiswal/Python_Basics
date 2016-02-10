##Sorting is an important basic algorithmic concept used to organize data so
##coders can better solve problems.
##Insertion Sort helpful in solving today's problem.
##The absolute difference between two integers, a and b, is |a−b|.
##The minimum absolute difference betn two integers in a list A of +ve integers,
##is the smallest absolute difference between any two integers in A.

T=int(raw_input().strip());
l = sorted([int(i) for i in raw_input().strip().split(' ')])
min_val=abs(l[0]-l[1]); tmp ='';
for i in range(1,len(l)):
    if min_val > abs(l[i-1]-l[i]): min_val = abs(l[i-1]-l[i]);
for i in range(1,len(l)):
    if min_val == abs(l[i-1]-l[i]): tmp +=str(l[i-1])+" "+str(l[i])+" "
    
#min_val = min(abs(y-x) for x,y in zip(sorted(l),sorted(l)[1:]))
#for x,y in zip(sorted(l),sorted(l)[1:]):
#    if abs(y-x)==min_val: tmp+="{0} {1} ".format(x,y);
print tmp.strip()
    
