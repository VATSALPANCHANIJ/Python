# For loop
# While Loop
# While Ture
# Nested Loop

# print("For loop")
# for i in range (2,11,2):
#  print(i)
#
# print("\n")

# number = int(input("Enter the value of table : - "))
# for i in range(1, 11,2):print(number,"*",i,"=",number * i)
# print("\n")
# print("While Loop")

# a = 1
# n = int(input("Enter the table value:- "))
# while a<=10:
#      print(n,"X",a, "=", n*a)
#      a+=2
#
# print("\n")
# print("While True loop")

#infinity loop system

while True:
    num1 = int(input("enter the number :- "))
    num2 = int(input("enter the number :- "))
    print(num1 + num2)
    repeat = input("do you want to stop the program: ")
    if repeat.lower() == "yes":
     break

    print("\n")
######################

# print("Nested Loops")
# for i in range (1,2):
#     for j in range (1, 11):
#         print(j)
#         print()
#
#
#      ##  pattern
#     for i in range (1,6):
#         for j in range (1, i+1):
#             print(j, end =" ")
#         print()

# Example
for i in range (1,121):
    if i % 8 == 0 and i % 12 ==0:
        print(i)

print("\n")
n = 1
while n <= 10:
     if n == 3:
       print("done")
     else:
      print(n)
     n += 1


