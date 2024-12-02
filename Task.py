# Write a program to get fibonacci series up to 10 numbers.

numbers = int(input("Enter the any numbers:"))
a = 0
b = 1
if numbers == 1:
    print(1)
else:
    for i in range(2,numbers):
        c = a + b
        a = b
        b = c
        print(c)
    print("Number of","1 to",numbers,"fibonacci series of  sum = ",c)

# Write a program to check if a number os prime or not.
numbers = int(input("Enter a number :"))
if numbers <= 1:
    print("It is not a prime number")
else:
    for i in range(2, numbers):
        if numbers % i == 0:
            print("Not a Prime number")
            break
        else:
            print("Prime number")
            break

# Write a program to find a palindrome of integers.

# example rev
"""
121 = 121
111 = 111
123 = 321
"""
# Write a program to create an area calculator.

