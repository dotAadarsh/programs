# Python Program to calculate the square root
import cmath

number = int(input("Enter the number: "))
number_sqrt = number ** 0.5
print("The square root of given number is: {}".format(number_sqrt))

# For real or complex numbers

num = eval(input("Enter the number: ")) # The eval() method can be used to convert complex numbers as input to the complex objects in Python. 
num_sqrt = cmath.sqrt(num)

print("The square root of {0} is {1:0.3}+{2:0.3}j".format(num, num_sqrt.real, num_sqrt.imag))