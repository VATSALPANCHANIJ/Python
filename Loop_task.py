# 1. Write a program to find a sum of all the even number up to 50.

sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += i

print("sum of all even number up to 100 is ",sum)
print("\n")
# 2. Write a program to write first 20 numbers and their squared numbers.
for i in range (1,20):
     print (i, i*i)

# 3. First 10 odd number sum using while loop

print("\n")
sum = 0
n = 0
while n <= 20:
    if n%2==1:
       sum += n
    n += 1
print("first 10 odd number sum :-",sum)
print("\n")

# 4. Write a program to check if a number us divisible by 8 and 10 up to 100 numbers

# 5. Write a program to create a billing system at supermarket.
