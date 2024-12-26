print('\t\tPRACTICAL-12')
print()
name=input('Enter the name  :')
try:
    if name.isalpha():
        print('THis is the Correct name')
    else:
        raise Exception('There is name error')
except Exception as e:
    print(e)
        
