#Solve the quadratic equation ax**2 + bx + c = 0
print('PRACTICAL-1')

print()
import cmath
a = 1
b = 14
c = 49
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
