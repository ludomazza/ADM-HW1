#!/usr/bin/env python
# coding: utf-8

# # Say "Hello, World!" With Python

# In[1]:


if __name__ == '__main__':
    print("Hello, World!")


# # Python If-Else

# In[2]:


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
n1=n%2
if n1!=0:
    print("Weird")
if n1==0 and n>=2 and n<=5:
    print("Not Weird")
if n1==0 and n>=6 and n<=20:
    print("Weird")
if n1==0 and n>20:
    print("Not Weird")


# # Arithmetic Operators

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# # Python: Division

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# # Loops

# In[3]:


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
        i+=1


# # Write a function

# In[ ]:


def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap


# # Print function

# In[4]:


if __name__ == '__main__':
    n = int(input())
print(*(i for i in range(1,n+1)),sep='')


# # List Comprehensions
# 
# 

# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    mix=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(mix) 


# # Find the Runner-Up Score!

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista=list(arr)
    scores=list()
    for i in lista:
        if i!=max(lista):
            scores.append(i)
        i+=1
    order=sorted(scores,reverse=True)
    print(order[0])


# # Nested Lists
# 
# 

# In[ ]:


if __name__ == '__main__':
    grades=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name,score])
    
    sorted_grades=sorted(list(set([x[1] for x in grades])))
    second_grade=sorted_grades[1]
    
    students=[]
    for student in grades:
        if second_grade==student[1]:
            students.append(student[0])
    
    for student in sorted(students):
        print(student)


# # Finding the percentage

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    sum=0
    for i in student_marks[query_name]:
        sum=sum+i
    mean=sum/3
    print("%.2f"%mean)


# # Lists

# In[ ]:


if __name__ == '__main__':
    N = int(input())
    command=[]
    for i in range(N):
        command.append(input().split())

    result=[]
    for i in range(N):
        if command[i][0]=='insert':
            result.insert(int(command[i][1]),int(command[i][2]))
        elif command[i][0]=='print':
            print(result)
        elif command[i][0]=='remove':
            result.remove(int(command[i][1]))
        elif command[i][0]=='append':
            result.append(int(command[i][1]))
        elif command[i][0]=='pop':
            result.pop()
        elif command[i][0]=='sort':
            result.sort()
        elif command[i][0]=='reverse':
            result.reverse()


# # Tuples

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    tupla=tuple(integer_list)
    print(hash(tupla))


# # sWAP cASE

# In[ ]:


def swap_case(s):
    if len(s) in range(0,1001):
        l=s.swapcase()
    return l


# # String Split and Join

# In[ ]:


def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# # What's Your Name?

# In[ ]:


def print_full_name(first, last):
    if len(first)<=10 and len(last)<=10:
        print("Hello"+" "+first+" "+last+"!"+" "+"You just delved into python.")


# # Mutations

# In[ ]:


def mutate_string(string, position, character):
    l=list(string)
    l[position]= character
    string=''.join(l)
    return string


# # Find a string

# In[ ]:


def count_substring(string, sub_string):
    count=0
    if len(string) in range (1,201):
        for i in range (0,len(string)):
            if string[i]==sub_string[0]:
                l=0
                for j in range(0,len(sub_string)):
                    if i+j>=len(string):
                        return count
                    if string[i+j]==sub_string[j]:
                        l+=1
                        if l==len(sub_string):
                            l=0
                            count+=1
    return count


# # String Validators

# In[ ]:


if __name__ == '__main__':
    s = input()
    
if len(s) in range (1,1001):
    print(any(i.isalnum() for i in s))

if len(s) in range (1,1001):
    print(any(i.isalpha() for i in s))

if len(s) in range (1,1001):
    print(any(i.isdigit() for i in s))
    
if len(s) in range (1,1001):
    print(any(i.islower() for i in s))

if len(s) in range (1,1001):
    print(any(i.isupper() for i in s))


# # Text wrap

# In[ ]:


def wrap(string, max_width):
    if len(string) in range(1,100):
        if max_width in range(1,len(string)):
            return textwrap.fill(string,max_width)


# # Designer Door Mat
# 

# In[ ]:


N, M = map(int, input().split())
if N in range (6,101):
    if M in range (16,303): 
        for i in range(1,N,2):
            print(str('.|.' * i).center(M,'-'))
        print('WELCOME'.center(M,'-'))
        for i in range(N-2,-1,-2):
            print(str('.|.' * i).center(M,'-'))


# # String Formatting

# In[ ]:


def print_formatted(number):
    l1 = len(bin(number)[2:])
   
    for i in range(1,number+1):
        print(str(i).rjust(l1),end=" ")
        print(oct(i)[2:].rjust(l1),end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1),end=" ")
        print(bin(i)[2:].rjust(l1),end=" ")
        print("")


# # Text Alignment
# 
# 

# In[ ]:


#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# # Alphabet Rangoli
# 
# 

# In[ ]:


import string
def print_rangoli(size):
    if size in range(1,27):
        design = string.ascii_lowercase
        L = []
        for i in range(n):
            s = "-".join(design[i:n])
            L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
        print('\n'.join(L[:0:-1]+L))


# # Capitalize!

# In[ ]:


# Complete the solve function below.
def solve(s):
    if len(s) in range(0,1000):
        return(" ".join([i.capitalize() for i in s.split(" ")]))


# # The Minion Game

# In[ ]:


def minion_game(string):
    if len(string) in range(1,(10**6)+1):
        stuart=0
        kevin=0
        l=len(string)
        for i in string:
            if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                kevin+=l
            else:
                stuart+=l
            l-=1
        
        if (kevin>stuart):
            print("Kevin", kevin)
        elif (kevin<stuart):
            print("Stuart", stuart)
        else:
            print("Draw")


# # Merge the Tools!

# In[ ]:


import textwrap
def merge_the_tools(string, k):
    i=0
    lista_sottostringhe=[]
    result = textwrap.wrap(string, k)
    while i < len(result):
        lista_sottostringhe.append(result[i])
        i+=1
    for parola in lista_sottostringhe:
        string=""
        doppie=[]
        for lettera in parola:
            if lettera not in doppie:
                string+=lettera
            if (parola.count(lettera)):
                doppie.append(lettera)
        print(string)


# # Introduction to Sets

# In[1]:


def average(array):
    if len(array) in range(0,101):
        a=set(array)
        somma=sum(a)
        totale=len(a)
        avg=round(float((somma/totale)),3)
        return avg


# # Symmetric Difference

# In[ ]:


m = input()
m_l= input()
newlis_m = list(map(int, m_l.split()))
myset_m = set(newlis_m)

n = input()
l_n=input()
newlis_n = list(map(int, l_n.split()))
myset_n = set(newlis_n)

m_n=myset_m.difference(myset_n)
n_m=myset_n.difference(myset_m)

diff=[]

for i in m_n:
    diff.append(i)
for j in n_m:
    diff.append(j)
    
for e in sorted(diff):
    print(e)


# # No Idea!

# In[ ]:


# 1) crea n,m = liste di numeri interi 

n,m= map(int,input().strip().split()) 
# map applica la funzione intero a n,m poi elimino tutti gli spazi in eccesso 
# con strip e, ogni singolo spazio che trova, interrompe lo scorrimento e crea una sottolista.
# MEMO: ad esempio, SPLIT(",") analizza la stringa e ogni virgola che incontra crea una sottostringa
# nel nostro caso ogni numero che incontra crea una sottostringa

# 2) creare un array che contiene n elementi
arr=list(map(int,input().strip().split()))

# 3) creo due set che conterranno m elementi
a_like=set(map(int,input().strip().split()))
b_dislike=set(map(int,input().strip().split()))

# 4) faccio un contatore per happiness
happiness=0

# 5) per ogni elemento che sta nell'array, controllo se sta in A o in B e 
# aumento/diminuisco il contatore

for i in arr:
    if i in a_like:
        happiness+=1
    elif i in b_dislike:
        happiness-=1

print(happiness)


# # Set.add()

# In[ ]:


paesi=set()
for i in range(int(input())):
    paesi.add(input())
print(len(paesi))


# # Set .discard(), .remove() & .pop()

# In[ ]:


n = int(input())
s = set(map(int, input().split()))
numero_comandi=int(input())

for i in range(numero_comandi): # numero di comandi da eseguire
    comandi=input().split() # lista dei comandi
    if comandi[0]=="discard": 
        s.discard(int(comandi[1])) # scarta il numero associato a quel comando
    elif comandi[0]=="remove":
        s.remove(int(comandi[1]))
    else:
        s.pop()
    
print(sum(s))


# # Set .union() Operation

# In[ ]:


n_eng=int(input())
matr_eng=set(input().split())

b_fr=int(input())
matr_fr=set(input().split())

entrambi=matr_eng.union(matr_fr)

somma=0

for i in entrambi:
    somma+=1
print(somma)


# # Set .intersection() Operation

# In[ ]:


n_eng=int(input())
matr_eng=set(input().split())

b_fr=int(input())
matr_fr=set(input().split())

entrambi=matr_eng.intersection(matr_fr)

somma=0

for i in entrambi:
    somma+=1
print(somma)


# # Set .difference() Operation

# In[ ]:


n_eng=int(input())
matr_eng=set(input().split())

b_fr=int(input())
matr_fr=set(input().split())

entrambi=matr_eng.difference(matr_fr)

somma=0

for i in entrambi:
    somma+=1
print(somma)


# # Set .symmetric_difference() Operation

# In[ ]:


n_eng=int(input())
matr_eng=set(input().split())

b_fr=int(input())
matr_fr=set(input().split())

entrambi=matr_eng.symmetric_difference(matr_fr)

somma=0

for i in entrambi:
    somma+=1
print(somma)


# # Set Mutations

# In[ ]:


n_a=int(input()) # numero elementi in A
set_a=set(map(int,input().split()))
n_b = int(input())

for i in range(n_b):
    comandi=input().split()
    set_b=set(map(int,input().split()))
    if comandi[0]=="update": 
        set_a.update(set_b)
    elif comandi[0]=="intersection_update":
        set_a.intersection_update(set_b)
    elif comandi[0]=="difference_update":
        set_a.difference_update(set_b)
    elif comandi[0]=="symmetric_difference_update":
        set_a.symmetric_difference_update(set_b)
    
print(sum(set_a))


# # The Captain's Room

# In[ ]:


k=int(input())
lista_camere=list(map(int,input().split()))
lista_camere_set=set(lista_camere)

dic={}

# dic[chiave]=valore

for x in lista_camere_set:
    dic[x]=0 # creo le chiavi con gli elementi del set

for y in lista_camere:
    dic[y]+=1 #conto quante volte le chiavi sono in lista camere

for x in dic.keys(): # scorro le chiavi e vedo quale ha un valore = 1
    if dic[x]==1:
        print(x)


# # Check Subset

# In[ ]:


t=int(input())

for x in range(t):
    t_a=input().split()
    set_a=set(map(int,input().split()))
    t_b=input().split()
    set_b=set(map(int,input().split()))

    print(set_a.issubset(set_b))


# # Check Strict Superset

# In[ ]:


set_a=set(map(int,input().split()))
n=int(input())
s=set()
for x in range(n):
    set_n=set(map(int,input().split()))
    s.update(set_n)
print(set_a.issuperset(s))


# # collections.Counter()

# In[ ]:


import collections 
n_shoes=int(input())
shoes=collections.Counter(list(map(int,input().split())))
n_costumers=int(input())

amount_money=0
for costumer in range(n_costumers):
    size,price=map(int,input().split())
    if shoes[size]:
        amount_money+=price
        shoes[size]-=1

print(amount_money)


# # DefaultDict Tutorial

# In[ ]:


from collections import defaultdict

# dict[chiave]=valore

n,m=map(int,input().split())
d=defaultdict(list)


for x in range(1,n+1):
    d[input()].append(str(x))
    

for y in range(1,m+1):
    words=input()
    if words in d:
        print(' '.join(d[words]))
    else:
        print(-1)


# # Collections.namedtuple()

# In[ ]:


from collections import namedtuple
n_stud=int(input())
s=list(input().split())
tot = 0

for student in range(n_stud):
    mark= int(list(input().split())[s.index('MARKS')])
    tot+=mark
    
print(tot/n_stud)


# # Collections.OrderedDict()

# In[ ]:


from collections import OrderedDict

n=int(input())
ordered_dictionary = OrderedDict()
for x in range(n):
    food_price=input().split()
    price=int(food_price[-1])
    food=' '.join(map(str,food_price[:-1]))

    if food in ordered_dictionary:
        ordered_dictionary[food]+=int(price)
    else:
        ordered_dictionary[food]=int(price)

for key,value in ordered_dictionary.items():
    print(key,value)
    


# # Word order

# In[ ]:


from collections import Counter
n=int(input())
ord_dict={}

for x in range(n):
    word=input()
    
    if word in ord_dict:
        ord_dict[word]+=1
    else:
        ord_dict[word]=1

        
print(len(ord_dict))
    
for x,y in ord_dict.items():
    print(y,end=' ')


# # Collections.deque()

# In[ ]:


from collections import deque

n=int(input())
d = deque()

for x in range(n):
    comandi=input().split()
    if comandi[0]=="append":
        d.append(int(comandi[1]))
    elif comandi[0]=="appendleft":
        d.appendleft(int(comandi[1]))
    elif comandi[0]=="clear":
        d.clear(int(comandi[1]))
    elif comandi[0]=="extend":
        d.extend(int(comandi[1]))
    elif comandi[0]=="extendleft":
        d.extendleft(int(comandi[1]))
    elif comandi[0]=="count":
        d.count(int(comandi[1]))
    elif comandi[0]=="pop":
        d.pop()
    elif comandi[0]=="popleft":
        d.popleft()
    elif comandi[0]=="remove":
        d.remove(int(comandi[1]))
    elif comandi[0]=="reverse":
        d.reverse(int(comandi[1]))
    elif comandi[0]=="rotate":
        d.rotate(int(comandi[1]))    

print(*d)


# # Company Logo

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()
    s=sorted(s)
    
    count=Counter(s)
    
    for x,y in count.most_common(3):
        print(x,y)
    


# # Piling up!

# In[ ]:


t =int(input())

for _ in range(t):
    n_cubes = int(input()) 
    sideLength = list(map(int,input().split()))
    stacking = "Yes"  
    for i in range(n_cubes // 2):           
        if max(sideLength[i],sideLength[n_cubes-i-1])<min(sideLength[i+1],sideLength[n_cubes-i-2]):
            stacking = "No"
    print(stacking)


# # Calendar Module

# In[ ]:


import calendar
data=input().split()

mese=int(data[0])
giorno=int(data[1])
anno=int(data[2])

calendario=calendar.weekday(anno,mese,giorno)

if calendario==0:
    print("MONDAY")


if calendario==1:
    print("TUESDAY")
    

if calendario==2:
    print("WEDNESDAY")
    

if calendario==3:
    print("THURSDAY")

if calendario==4:
    print("FRIDAY")

if calendario==5:
    print("SATURDAY")

if calendario==6:
    print("SUNDAY")


# # Time Delta

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime 
# Complete the time_delta function below.
def time_delta(t1, t2):
    formato = "%a %d %b %Y %H:%M:%S %z"
    t1_datetime = datetime.strptime(t1, formato)
    t2_datetime = datetime.strptime(t2, formato)
    
    return str(abs(int((t1_datetime - t2_datetime).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# # Exceptions

# In[ ]:


t = int(input());
for x in range(t):
    try:
        a, b = input().split()
        print(int(a)//int(b))
    except ZeroDivisionError as ZDE:
        print("Error Code:",ZDE);
    except ValueError as VE:
        print("Error Code:",VE);


# # Zipped!

# In[ ]:


N,X=input().split()
lista_voti=[]
for i in range(int(X)):
    student_marks=map(float,input().split())
    lista_voti.append(student_marks)

for voti in zip(*lista_voti):
    print (sum(voti)/len(voti))


# # ginortS

# In[ ]:


Stringa=input()
upper=""
lower=""
even=""
odd=""

for carattere in Stringa:
    if carattere.isupper():
        upper+=carattere
    elif carattere.islower():
        lower+=carattere
    else:
        if int(carattere)%2==0:
            even+=carattere
        else:
            odd+=carattere

all_sorted=sorted(lower)+sorted(upper)+sorted(odd)+sorted(even)
            
print(''.join(all_sorted))


# # Athlete Sort

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())


    tab_sort=sorted(arr,key=lambda row:row[k])
    for i in range(len(tab_sort)):
        for j in range(len(tab_sort[i])):
            print(tab_sort[i][j], end=' ')
        print()


# # Map and Lambda Function

# In[ ]:



cube = lambda x: x**3   

def fibonacci(n):
    lista_fibonacci=[]
    fib_0, fib_1=0,1
    for x in range(n):
        lista_fibonacci.append(fib_0)
        fib_0,fib_1=fib_1,fib_0+fib_1
    return lista_fibonacci


# # Arrays

# In[ ]:


import numpy

def arrays(arr):
    f=numpy.array(arr,float)
    rev_arr=numpy.flip(f)
    return rev_arr


# # Shape and Reshape

# In[ ]:


import numpy

n=input().split()
arr=numpy.array(n,int)


print(numpy.reshape(arr,(3,3)))


# # Transpose and Flatten

# In[ ]:


import numpy
N,M=map(int,input().split())
mat=[]
for x in range(N):
    m=list(map(int,input().split()))
    mat.append(m)

mat_arr=numpy.array(mat)
print(numpy.transpose(mat_arr))
print(mat_arr.flatten())


# # Concatenate

# In[ ]:


import numpy
n,m,p=map(int,input().split())
l=[]
s=[]
for x in range(n):
    l.append(list(map(int,input().split())))

for y in range(m):
    s.append(list(map(int,input().split())))
    

l_arr=numpy.array(l)
s_arr=numpy.array(s)

print (numpy.concatenate((l_arr, s_arr), axis = 0))


# # Zeros and Ones

# In[ ]:


import numpy

line=input().split()

arr=numpy.array(line,int)


print(numpy.zeros(arr,dtype=int))

print(numpy.ones(arr,dtype=int))


# # Eye and Identity

# In[ ]:


import numpy
numpy.set_printoptions(legacy='1.13')

N,M=input().split()

arr_N=numpy.array(N,int)
arr_M=numpy.array(M,int)

print(numpy.eye(arr_N,arr_M,k=0))


# # Array Mathematics

# In[ ]:


import numpy
N,M=map(int,input().split())

lista_a=[]
lista_b=[]
for _ in range(N):
    lista_a.append(list(map(int,input().split())))
for _ in range(N):
    lista_b.append(list(map(int,input().split())))

A=numpy.array(lista_a)
B=numpy.array(lista_b)


funzioni =[numpy.add(A,B), numpy.subtract(A,B), numpy.multiply(A,B), numpy.floor_divide(A,B), numpy.mod(A,B), numpy.power(A,B)]

for funzione in funzioni:
    print(funzione)


# # Floor, Ceil and Rint

# In[ ]:


import numpy
numpy.set_printoptions(legacy='1.13')
A=input().split()

A=numpy.array(A,float)

print(numpy.floor(A))

print(numpy.ceil(A))
print(numpy.rint(A))


# # XML 1 - Find the Score

# In[ ]:


import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    a=len(node.attrib)
    for x in node:
        a+=get_attr_number(x)
    return a

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# # XML2 - Find the Maximum Depth

# In[ ]:


import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if level >= maxdepth:
        maxdepth+=1
    for x in elem:
        depth(x,level+1)
    
    

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# # Standardize Mobile Number Using Decorators

# In[ ]:


def wrapper(f):
    def fun(l):
        lm = lambda p: '+91 ' + p[-10:-5] + ' ' + p[-5:]
        f(map(lm, l))

    return fun
@wrapper 

def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# # Decorators 2 - Name Directory

# In[ ]:


import operator
from operator import itemgetter


def person_lister(f):
    def inner(people):
        for x in people:
            x[2] = int(x[2])
        people.sort(key=itemgetter(2))
        return map(f,people)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# # Sum and Prod

# In[ ]:


import numpy

N,M=map(int,input().split())
lista=[]

for _ in range(N):
    lista.append(input().split())

arr=numpy.array(lista,int)

print(numpy.prod(numpy.sum(arr,axis=0)))


# # Min and Max

# In[ ]:


import numpy

N,M=map(int,input().split())
lista=[]

for _ in range(N):
    lista.append(input().split())

arr=numpy.array(lista,int)

print(numpy.max(numpy.min(arr,axis=1)))


# # Mean, Var, and Std

# In[ ]:


import numpy

N,M=map(int,input().split())
lista=[]

for _ in range(N):
    lista.append(input().split())

arr=numpy.array(lista,int)

print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(numpy.around(numpy.std(arr),11))


# # Dot and Cross

# In[ ]:


import numpy

N=int(input())
lista_a=[]
lista_b=[]
for _ in range(N):
    lista_a.append(input().split())

for _ in range(N):
    lista_b.append(input().split())

arr_a=numpy.array(lista_a,int)
arr_b=numpy.array(lista_b,int)

print(numpy.dot(arr_a,arr_b))


# # Inner and Outer

# In[ ]:


import numpy

A=numpy.array(list(map(int,input().split())))
B=numpy.array(list(map(int,input().split())))

print(numpy.inner(A,B))
print(numpy.outer(A,B))


# # Polynomials

# In[ ]:


import numpy

P=numpy.array(list(map(float,input().split())))
x=int(input())

print(numpy.polyval(P,x))


# # Linear Algebra

# In[ ]:


import numpy

n=int(input())
lista=[]
for _ in range(n):
    lista.append(list(map(float,input().split())))
    
a=numpy.array(lista)
print (numpy.around((numpy.linalg.det(a)),2))


# # Birthday Cake Candles

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    lista=[]
    for i in candles:
        lista.append(i)
    a=lista.count(max(lista))
    return a
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())
    

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# # Number Line Jumps

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    diff_pos=x2-x1 # differenza tra le posizioni da cui partono i canguri
    i=0
    while diff_pos>=i:
        x1+=v1
        x2+=v2
        
        if (x1==x2):
            return "YES"
        i+=1
    
    return "NO"
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# # Viral Advertising

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    like_cumulati=0 
    condivisione=5  
    for i in range(1,n+1):     
        like_del_giorno =condivisione//2  
        like_cumulati+=like_del_giorno 
        condivisione=like_del_giorno*3 
    return like_cumulati
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# # Recursive Digit Sum

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    if(len(n)==1 and k==1):
        return int(n)
    else:
        somma = sum(list(map(int,n)))
        return superDigit(str(somma*k),1)
        
    
    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# # Insertion Sort - Part 1

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
        for i in range((n-1),0,-1):
            if arr[i]<arr[i-1]:
                lista=arr[i]
                arr[i]=arr[i-1]
                print(*arr)
                arr[i-1]=lista
        print(*arr)
                
                

            
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# # Insertion Sort - Part 2

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        print(*arr)

            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


# # Detect Floating Point Number

# In[ ]:


import re
N=int(input())
for x in range(N):
    if re.search(r"^[+-]?[0-9]*\.[0-9]+$", input()):
        print("True")
    else:
        print("False")


# # Re.split()

# In[ ]:


regex_pattern = r"[,.]+"	# Do not delete 'r'.



import re
print("\n".join(re.split(regex_pattern, input())))


# # Group(), Groups() & Groupdict()

# In[ ]:


import re
s=input()
cerca_caratteri=re.findall(r"([A-Za-z0-9])\1+",s)
if cerca_caratteri:
    print(cerca_caratteri[0])
else:
    print(-1)


# # Re.findall() & Re.finditer()

# In[ ]:


import re
s=input()
match= re.findall(r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])", s)

if match ==[]:
    print(-1)
else:
    print(*match, sep="\n")


# # Re.start() & Re.end()

# In[ ]:


import re

s=input()
k=input()
match="No"

for x in re.finditer(r'(?=('+k+'))',s):
    match = 'Yes'
    start=x.start(1)
    end=x.end(1)-1
    print ((start,end))
if match == 'No':
    print ((-1, -1))


# # Regex Substitution

# In[ ]:


import re

N=int(input())

for x in range(N):
    s=input()
    while re.search(r"(\s&&\s)", s):
        s = re.sub(r"(\s&&\s)", " and ", s)
    while re.search(r"(\s\|\|\s)", s):
        s = re.sub(r"(\s\|\|\s)", " or ", s)
    print(s)


# # Validating Roman Numerals

# In[ ]:


regex_pattern = r"(M{0,3})(C[DM]|D?C{0,3})(X[LC]|L?X{0,3})(I[VX]|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))


# # Validating phone numbers

# In[ ]:


import re
n=int(input())

for x in range(n):
    number=input()
    if re.match(r"^[789]\d{9}$",number):
        print("YES")
    else:
        print("NO")


# # Validating and Parsing Email Addresses

# In[ ]:


import re
n=int(input())

for i in range(n):
    name,email=input().split()
    control= r"<[a-z][a-zA-Z0-9\-\.\_]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}>"

    if (re.search(control,email)):
        print(name,email)
            


# # Hex Color Code

# In[ ]:


import re

n=int(input())

for x in range(n):
    CSS=input()
    control=re.compile(r"[\s:](#(?:[0-9A-Fa-f]{3}){1,2})")
    a=control.findall(CSS)
    if a:
        print(*a, sep='\n')


# # HTML Parser - Part 1

# In[ ]:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr1,attr2 in attrs:
            print(f"-> {attr1} > {attr2}")


    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr1, attr2 in attrs:
            print(f"-> {attr1} > {attr2}")

n = int(input())
stringa = ""
for i in range(n):
    html = input()
    stringa += html
parser = MyHTMLParser()
parser.feed(stringa)


# # HTML Parser - Part 2

# In[ ]:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data != '\n':
            if "\n" in data:
                print(">>> Multi-line Comment")
                print(data)
            else:
                print(">>> Single-line Comment")
                print(data)
    def handle_data(self, data):
        if not data == '\n':
            print(f">>> Data")
            print(data)
  
  

  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# # Detect HTML Tags, Attributes and Attribute Values

# In[ ]:


from html.parser import HTMLParser
class CustomHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])


parser = CustomHtmlParser()
n=int(input())
for x in range(n):
    parser.feed(input())


# # Validating UID

# In[ ]:


import re

t=int(input())

for x in range(t):
    UID=input()
    if (UID.isalnum()) and (len(set(UID)) == 10) and         (re.match('(.*[A-Z].*){2}', UID) != None) and         (re.match('(.*[0-9].*){3}', UID) != None):
        print("Valid")
    else:
        print("Invalid")


# # Validating Credit Card Numbers

# In[ ]:


import re

n=int(input())
for x in range(n):
    credit_card=input()
    if (re.match(r"^[456]\d{3}(-?\d{4}){3}$", credit_card) and          not re.search(r"([0-9])(-?\1){3}", credit_card)):
        print("Valid")
    else:
        print("Invalid")


# # Validating Postal Codes

# In[ ]:


regex_integer_in_range = r"^[1-1][0-9][0-9][0-9][0-9][0-9]$|^[2-9][0-9][0-9][0-9][0-9][0-9]$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)" # Do not delete 'r'.


# # Matrix Script

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

elem = list(zip(*matrix))
string = ""
for i in range(len(elem)):
    string += "".join(elem[i])
pattern = re.compile(r"(?<=\w)[!@#$%& ]{1,}(?=\s*\w)")
new_string = re.sub(pattern," ",string)
print(new_string)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




