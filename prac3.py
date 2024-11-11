def pyramid(n):

    for i in range(n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    print()
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
n = int(input("Enter the number of rows: "))

pyramid(n)
