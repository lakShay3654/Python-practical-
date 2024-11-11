
def check():
    n=int(input("Enter the number:"))
    for i in range(2,n):
        if n%i==0:
            print("It's not a prime number")
            break
    else:
        print(n, 'is a prime number')
    if n==1:
        print('1 is not a prime number')


def gen():
    n=int(input("Enter the number"))
    for i in range(1,n+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
                    
            else: 
                print(i, end =',')

def generate_primes(n):
    primes = []
    num = 2

    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1

    return primes

n = int(input("Enter the number of prime numbers to generate: "))

generate_primes(n)


