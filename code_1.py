from itertools import permutations
from itertools import combinations
import numpy as np
word=input("Enter the input letters: ")
word=word.upper()
x=0
length=int(input("Enter the length of the word you want to find: "))
x=int(input("Enter if any contraits:\n1.Yes\n2.No "))
if(x==1):
    noc=int(input("Enter the number of contraints: "))
    arr=np.empty((noc,2),dtype=object)
    print("Enter the blank index and letter\nEx:5,A: ")
    for j in range(0,noc):
        str=input()
        a=int(str[0])-1
        arr[j][0]=a
        arr[j][1]=str[2].upper()   
sat=0       
leng=len(word)
s=set()
with open("wordList.txt","r") as file:
    res=file.read().split()  
for c in combinations(word,length):
# comb=set(c)
    comb="".join(c)
    # print(comb)
    for p in permutations(comb):
        perm="".join(p)
        if(x==1):
            for j in range(0,noc):
               if(perm[arr[j][0]]==arr[j][1]):
                   sat=1
               else:
                   sat=0
                   break
            if(sat==1 and (perm in res)):
                s.add(perm)
        if(perm in res and x==2):
            s.add(perm)
if(x==1 or x==2):
    print("The posiible words are: ",s)
    print("DONE")
if(x!=1 and x!=2):
    print("Chose the valid input")