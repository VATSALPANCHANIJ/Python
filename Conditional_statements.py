# if the statements
# if-else statements
# if-elif-else statements
# Nested statement
# short Hand if Statement

########################

print("If statement")

mark = 99
if mark <= 100:
    print('Good Work')

print("Keep it up")

print("\n")

########################

print("If-else Statement")

total = 60
if total >=80:
       print("Good")
else:
      print("Better luck next time")

      print("\n")

########################

print("if-elif-else statements")
marks = 98
if marks >=90:
       print("A Grad 🔖")
elif marks >= 80 and marks < 90:
      print("B Grad 😎")
elif marks >= 70 and  marks < 80:
      print("B+ Grad 📔")
elif marks >= 60 and marks < 70:
      print("C Grad 📚")
else:
      print("👍👍👍👍 Better luck next time")

print("\n")
########################
print("Nested if Statement")
marks = 80
if marks >=90:
   print("A+")
if marks >=95:
   print("With Trip")
else:
   print("No Trip")

print("\n")
########################
print("Short Hand if statement")

marks = 90
if marks >=80: print("Well Done")
print("#################")
print("short Hand if-else statement")
marks = 88
print("Good")if marks >80 else print("Not Good")


#TASK

#vowel numbers

letter = input("Enter a Letter for check Vowel text: ")
if (letter in "aeiou") or (letter in "AEIOU"):
     print("It is a Vowel")
else:
 print("It is a not Vowel")

print("\n")
#find the number lenght example (1 digits, 2 digits, 3 digits etc.........

num =int( input("Enter the number: "))
if num >=0 and num <=9:
     print("1 Digits Number")
elif num >=10 and num <=99:
     print("2 Digits Number")
elif num >=100 and num <=999:
     print("3 Digits Number")
