print("(a)Print whether the character is a letter or numeric digit or a special character\n(a)If the character is a letter, print whether the letter is uppercase or lowercase\n(c)If the character is a numeric digit, Print its name in text")
c=input('Enter the character\t:')
d={0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

if c>='A' and c<='Z':
    print('Its Uppercase')
elif c>='a' and c<='z':
    print('Its Lower case')
elif c>='0' and c<='9':
    print('Its a Numeric Value')
    n=int(c)
    print(d[n])
else:
    print('Special Character')
