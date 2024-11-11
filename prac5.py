def frequency():
    s=input('ENTER THE STRING\t:')
    count=0
    c=input('ENTER THE CHARACTER\t:')
    for i in s:
        if i== str(c):
            count+=1
        else:
            pass
    print('The Frequency of the character is',count)


def replace():
    s=input('Enter the Sting\t\t\t:')
    oldchar=input('Enter the character you want to replace\t\t:')
    newchar=input('Enter the character to be replaced with\t\t:')
    s1=s.replace(oldchar,newchar)
    print('The New String is',s1)

def remove():
    s=input('Enter the Sting\t:')
    char=input('Enter the charcter\t:')
    for i in s:
        if i!=char:
            pass
        else:
            s1 = s.replace(char,"",1)
            break
    print('The New String is :',s1)

def remove1():
    s=input('Enter the Sting\t:')
    char=input('Enter the charcter\t:')
    for i in s:
        if i!=char:
            pass
        else:
            s1 = s.replace(char,"")
            break
    print('The New String is :',s1)
remove1()

