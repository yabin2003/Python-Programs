
#1. Frequency of characters in a string
'''s="programming"
d={}
for i in s:
    if i not in d.keys():
        d[i]=0
    d[i]+=1
for i in d.items():
    print(i)'''
import math
#2. Target sum
'''
a=[3,5,6,2,7,8]
t=8
a.sort()
n=len(a)
def tgsum(a,t,n):
    for i in range(n):
        for j in range(i+1,n-1):
            if(a[i]+a[j]==t):
                return (i,j)
    return -1
def bs(a,t,n):
    l,r=0,n-1
    while(l<=r):
        m=l+(r-l)//2
        if(a[m]==t):
            return m
        elif(a[m]<t):
            l=m+1
        else:
            r=m-1
    return -1
print(bs(a,t,n))
'''
# Sorting Algorithms

#1. Bubble sort:--------------------------------------------------
'''
a=[4,1,3,6,7,2,10,9,20,2,1,2,1]
n=len(a)
def bubble_sort(a,n):
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

# 2. Selection sort:-------------------------------------------------

def selection_sort(a,n):
    for i in range(n):
        m=i
        for j in range(i+1,n):
            if a[m]>a[j]:
                m=j
            a[i],a[m]=a[m],a[i]
    return a

def ss(a,n):
    for i in range(n):
        for j in range(i+1,n):
            if(a[i]>a[j]):
                a[i],a[j]=a[j],a[i]
    return a
'''
# Merge Sort:
'''
a=[3,6,8,9,2,1]
n=len(a)
def merge_sort(a,n):
    if n>1:
        mid=n//2
        left=a[:mid]
        right=a[mid:]

        merge_sort(left,len(left))
        merge_sort(right,len(right))

        i=j=k=0
        while(i<len(left) and  j<len(right)):
            if (left[i]<right[j]):
                a[k]=left[i]
                i+=1
            else:
                a[k]=right[j]
                j+=1
            k+=1

        while(i<len(left)):
            a[k]=left[i]
            i+=1
            k+=1

        while (j < len(right)):
            a[k] = right[j]
            j+=1
            k+=1

    return a
print(merge_sort(a,n))
'''

#Quick sort:

'''
a=[2,5,3,7,9,8]
def quick_sort(a):
    if len(a)<=1:
        return a
    p=a[len(a)//2]
    l=[x for x in a if x<p]
    m=[x for x in a if x==p]
    r=[x for x in a if x>p]

    return quick_sort(l)+m+quick_sort(r)
print(quick_sort(a))

'''

#Insertion sort:
'''
a=[2,3,5,7,1,9]
n=len(a)
def inertion_sort(a,n):
    for i in range(1,n):
        k=a[i]
        j=i-1
        while j>=0 and k<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=k
    return a
print(inertion_sort(a,n))
'''
# Sub array:--------------------------------------
'''
def sub_array(a,n):
    res=[]
    for i in range(n):
        for j in range(i+1,n):
            res.append(a[i:j+1])
    print(res)
    print(len(res))
sub_array(a,n)

# Binary Search or target sum:------------------------------------------
a=[1,4,5,6,2,9,10]
n=len(a)
t=8
def binary_search(a,t,n):
    l,r=0,n-1
    while(l<=r):
        m=l+(r-l)//2
        if(a[l]+a[r]==t):
            l+=1
            r-=1
        elif(a[l]+a[r]<t):
            l=m+1
        else:
            r=m-1
    return (l,r)
print(binary_search(a,t,n))
'''


#Binary Search

# 1. Finding the element in an array:
'''
a=[3,5,8,7,10,34]
t=10
n=len(a)
def bs(a,n,t):
    l,r=0,n-1
    while(l<=r):
        m=l+(r-l)//2
        if(a[m]==t):
            return m
        elif(a[m]<t):
            l=m+1
        else:
            r=m-1
    return m
print(bs(a,n,t))
------------------------------------------------------------------------
'''

# 2. Target sum
'''
a=[3,5,8,7,10,34]
t=15
def bs(a,t):
    l,r=0,len(a)-1
    while(l<=r):
        if(a[l]+a[r]==t):
            return (l,r)
            r-=1
            l+=1
        elif(a[l]+a[r]<t):
            l+=1
        else:
            r-=1
print(bs(a,t))
------------------------------------------------------------------------
'''

# 3. Reverse the vowels in a string in actual place:

'''
s='Yabin Joel'
s=list(s)
v="aeiouAEIOU"
stack=[i for i in s if i in v]
print(stack)
for i in range(len(s)):
    if s[i] in v:
        s[i]=stack.pop()

print(''.join(s))
-----------------------------------------------------------------------
'''

#4. Occurences of the words in a string:

'''
s="yabin joel joel yabin y h y "
li=s.split()
d={}
for i in li:
    if i not in d.keys():
        d[i]=0
    d[i]+=1
print(d)
-----------------------------------------------------------------------
'''

#5. Occurences of the each letters in a string:
'''
s=input("Enter a string : \t")
c={}
for i in s:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
for key,value in c.items():
    print(f"{key} occurs {value} times")
-----------------------------------------------------------------------
'''
# 6. Finding the position of the letter in a string:
'''
s="Yabin Joel"
t='n'
s=list(s)
def bs(s,t):
    l,r=0,len(s)-1
    while(l<=r):
        m=l+(r-l)//2
        if(s[m]==t):
            return (s[m],m)
        elif(s[m]<t):
            l=m+1
        else:
            r=m-1
    return 'not found'
print(bs(s,t))
------------------------------------------------------------------------
'''
 # 7. Prime number
'''
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=18
a=[]
res=1
for i in range(2,n+1):
    if(is_prime(i)):
        a.append(i)
        res*=i
print(a)
print(res)

--------------------------------------------------------------------------
'''
# 8. Find the missing number in the array:
'''
a=[1,5,6,8,4,2,3]
a.sort()
s=0
for i in range(len(a)-1):
    if a[i]!=a[i+1]-1:
        s=a[i]+1
print(s)
---------------------------------------------------------------------------
'''

# 9. Happy Number:
'''
def result(n):
    s=set()
    while(n!=1 and n not in s):
        s.add(n)
        n=sum(int(i)**2 for i in str(n))
    return n==1
print(result(19))
print(result(20))

---------------------------------------------------------------------------
'''

# 10. Factorial of a number:
'''
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))
print(fact(3))
print(fact(6))

'''
#11. Fibonacci of a number:
'''
def fibonacci(n):
    r=[0,1]
    for i in range(2,n+1):
        r.append(r[i-1]+r[i-2])
    return r[:n]
print(fibonacci(10))
'''

#12. Find the gcd and lcm:
'''

a,b=12,18
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
print(gcd(a,b))

def lcm(a,b):
    return (a*b)//gcd(a,b)
print(lcm(a,b))

'''


#Searching algorithms:

#linear search:

'''
a=[2,5,3,6,8,9,4,10]
n=len(a)
t=10

def linear_Search(a,t,n):
    for i in range(n):
        if a[i]==t:
            return i
print(linear_Search(a,t,n))'''

# Binary Search:
'''
def binary_search(a,t,n):
    l,r=0,n-1
    while(l<=r):
        m=l+(r-l)//2
        if(a[m]==t):
            return m
        elif(a[m]<t):
            l=m+1
        else:
            r=m-1
    return -1
print(binary_search(a,t,n))

'''

# Merge Twp sorted lists:
'''
l1=[1,2,3,4]
l2=[5,6,7,8,9]

def res(l1,l2):
    i,j=0,0
    mg=[]
    while(i<len(l1) and j<len(l2)):
        if l1[i]<l2[j]:
            mg.append(l1[i])
            i+=1
        else:
            mg.append(l2[j])
            j+=1

        mg.extend(l1[i:])
        mg.extend(l2[j:])
        return mg
print(res(l1,l2))

'''
# Find the Majority Element in a array:

'''
li=[1,4,3,3,2,4,5,3,3,3,4,6,7]
n=len(li)
d={}
r=[]
def majority_element(li,n):
    for i in li:
        if i not in d:
            d[i]=0
        d[i]+=1
    m=max(d,key=d.get)
    print(m)
majority_element(li,n)

'''

# Count the elements with maximum frequency:

'''
li=[1,1,3,2,2,4]
n=len(li)
d={}
r=[]
def majority_element(li,n):
    for i in li:
        if i not in d:
            d[i]=0
        d[i]+=1
    m=max(d.values())
    for key,value in d.items():
        if value==m:
            r.append(key)
    print(len(r)
majority_element(li,n)


from operator import index
nums=[2,7,1,19,18,3]
n=len(nums)
li=[]
for i in nums:
    if n%index(i)==0:
        li.append(i)

s=sum(int(i)**2 for i in li)
print(s)
print(li)
'''

# Armstrong number:----------------------------------------------
'''
def armstrong_number(n):
    d=[i for i in str(n)]
    p=len(d)
    s=sum(int(i)**p for i in d)
    return s==n

#Neon number:----------------------------------------------------

def neon_number(n):
    sq=n**2
    s=sum(int(i) for i in str(sq))
    return s==n
print(neon_number(9))

#Perfect number:------------------------------------------------

def perfect_number(n):
    d=[i for i in range(1,n) if n%i==0]
    return n==sum(d)
print(perfect_number(28))

'''

# Print the right rotated array k times:--------------------------------
'''
#Right:

a=[1,5,4,3,6,2]
k=2
n=len(a)
k=k%n
res=a[-k:]+a[:-k]
print(res)

#Left:

rot=a[k:]+a[:k]
print(rot)

'''

#Maximum Sum of sub array of size k:
'''
a=[1,4,2,5,6,7,8,4]
k=3

def sum_sub_arr(a,k):
    n=len(a)
    maxsum=0
    currsum=0
    for i in range(k):
        currsum+=a[i]
    maxsum=currsum

    for i in range(k,n):
        currsum+=a[i]-a[i-k]
        maxsum=max(maxsum,currsum)
    return maxsum
print(sum_sub_arr(a,k))

'''

#Reverse of Array in various approach:---------------------------------------------
'''
a=[1,2,3,4,5]
n=len(a)

# Two pointer approach:--------

l,r=0,n-1

while l<r:
    a[l],a[r]=a[r],a[l]
    l+=1
    r-=1
print(a)
'''

# Swapping elements:----------
'''
for i in range(n//2):
    temp=a[i]
    a[i]=a[n-i-1]
    a[n-i-1]=temp
    print(a)
print(a)

'''

# count the vowles in the substrings:
'''
a="aba"
a=list(a)
n=len(a)
def sub_array(a,n):
    res=[]
    for i in range(n):
        res.append(a[i])
        for j in range(i+1,n):
            res.append(a[i:j+1])
    print(res)
    print(len(res))
    v="aeiou"
    c=0
    for i in res:
        for j in i:
            if j in v:
                c+=1
    print(c)
sub_array(a,n)

'''









































