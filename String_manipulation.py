# Slicing
# Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"
a = "Hello, World!"
print(b[2:5])

# Slice From the Start
print(b[:5])
# Slice To the End
print(b[2:])

# Negative Indexing
print(b[-5:-2])

# Remove Whitespace
print(a.strip()) # returns "Hello, World!"

# Replace String
print(a.replace("H", "J"))


# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

print(a.split(",")) # returns ['Hello', ' World!']


# F-Strings  -------  String Format

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as
# placeholders for variables and other operations.

age = 36
txt = f"My name is John, I am {age}"
print(txt)



# Escape Character
# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."


# Other all Methods


""" capitalize()	Converts the first character to upper case

casefold()	Converts string into lower case

center()	Returns a centered string

count()	Returns the number of times a specified value occurs in a string

encode()	Returns an encoded version of the string

endswith()	Returns true if the string ends with the specified value

expandtabs()	Sets the tab size of the string

find()	Searches the string for a specified value and returns the position of where it was found

format()	Formats specified values in a string

format_map()	Formats specified values in a string

index()	Searches the string for a specified value and returns the position of where it was found

isalnum()	Returns True if all characters in the string are alphanumeric

isalpha()	Returns True if all characters in the string are in the alphabet

isascii()	Returns True if all characters in the string are ascii characters

isdecimal()	Returns True if all characters in the string are decimals

isdigit()	Returns True if all characters in the string are digits

isidentifier()	Returns True if the string is an identifier

islower()	Returns True if all characters in the string are lower case

isnumeric()	Returns True if all characters in the string are numeric

isprintable()	Returns True if all characters in the string are printable

isspace()	Returns True if all characters in the string are whitespaces

istitle()	Returns True if the string follows the rules of a title

isupper()	Returns True if all characters in the string are upper case

join()	Joins the elements of an iterable to the end of the string

ljust()	Returns a left justified version of the string

lower()	Converts a string into lower case

lstrip()	Returns a left trim version of the string

maketrans()	Returns a translation table to be used in translations

partition()	Returns a tuple where the string is parted into three parts

replace()	Returns a string where a specified value is replaced with a specified value

rfind()	Searches the string for a specified value and returns the last position of where it was found

rindex()	Searches the string for a specified value and returns the last position of where it was found

rjust()	Returns a right justified version of the string

rpartition()	Returns a tuple where the string is parted into three parts

rsplit()	Splits the string at the specified separator, and returns a list

rstrip()	Returns a right trim version of the string

split()	Splits the string at the specified separator, and returns a list

splitlines()	Splits the string at line breaks and returns a list

startswith()	Returns true if the string starts with the specified value

strip()	Returns a trimmed version of the string

swapcase()	Swaps cases, lower case becomes upper case and vice versa

title()	Converts the first character of each word to upper case

translate()	Returns a translated string

upper()	Converts a string into upper case

zfill()	Fills the string with a specified number of 0 values at the beginning

"""