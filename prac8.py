def cubes():
    L=[]
    L1=eval(input('Enter the list\t:'))

    for i in L1:
        if type(i)==int:
            if i%2==0:
                L.append(i**3)
    print(L)
cubes()