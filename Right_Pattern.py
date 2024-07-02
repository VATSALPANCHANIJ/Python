# 1. Pattern
"""
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
"""
for i in range (1,6):
    for j in range (5,i,-1):
        print(" " ,end = " ")
    for p in range (i):
        print(i,end=" ")
    print()
print("*********")
for  i in range (1,6):
    for j in range(5, i, -1):
        print(" ", end = " ")
    for p in range (i):
        print("*", end=" ")
    print()
print("**********")
# 2. Pattern
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ", end=" ")
    for p in range(i):
        print(i, end=" ")
    print()

# 3.Pattern
"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        *
"""
print("|||||||||||||||||||")
for i in range(1,5):
    for j in range(5,i,-1):
        print(" ", end=" ")
    for p in range (i):
        print("*", end=" ")

    print()

for i in range(5,0,-1):
    for j in range(5-i):
        print(" ", end=" ")
    for p in range(i):
        print("*", end=" ")
    print()

# Mix Pattern
print("|||||||||||||||||||")
"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
"""
for i in range(5):
    for j in range(5-i-1):
        print(" ", end=" ")
    for p in range(2*i+1):
        print("*",end=" ")
    print()

print("|||||||||||||||||||")
"""
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          *
"""
for i in range(6 - 1):
    for j in range(i + 1):
        print(" ",end=" ")
    for g in range(2 * (6 - i - 1) - 1):
        print("*", end=" ")
    print()
print("|||||||||||||||||||")

# Diamond Shape
"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
"""
for i in range(5):
    for j in range(5-i-1):
        print(" ", end=" ")
    for p in range(2*i+1):
        print("*",end=" ")
    print()

for i in range(5 - 1):
        for j in range(i + 1):
            print(" ", end=" ")
        for g in range(2 * (5 - i - 1) - 1):
            print("*", end=" ")
        print()