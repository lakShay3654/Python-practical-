#Write a function that accepts two string and returns the indices of all the occurences of the second string in the first string as a list. 
#If the second string is not present in present in first string then it should return -1.

def occ(a,b): 
    newlist =[]
    if b not in a:
         print(-1) 
    else: 
        i=0 
        while i< len(a): 
            c=a.find(b,i) 
            if c==-1: 
                break
            i=c+ len(b)
            newlist.append(c) 
        print(newlist)
a=input('Enter first String\t:')
b=input('Enter second String\t:')
occ(a,b)

