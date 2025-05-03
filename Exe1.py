# (1) What is 7 to the power of 4?
print(7**4)

# (2) Split this string:
# s = "Hi there Sam!"
# into a list.
s = "Hi there Sam!"
list[s]
print(s)

# (3) Given the variables:
# planet = "Earth"
#       diameter = 12742
# Use .format() to print the following string:
# The diameter of Earth is 12742 kilometers
planet = "Earth"
diameter = 12742

print("The diameter of {} is {} kilometers".format(planet,diameter))

# (4) Given this nested list, use indexing to grab the word "hello"
# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

# (5) Given this nested dictionary grab the word "hello".
# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
lst= d['k1']
lst1 = lst[3]
lst2 = lst1['tricky']
lst3 = lst2[3]
lst4 = lst3['target']
lst5 = lst4[3]
print(lst5)

#(6) What is the main difference between a tuple and a list?
tu_ple = (1,2,3,4,5)
li_st = [1,2,3,4,5]

print(type(tu_ple))
print(type(li_st))

try:
    tu_ple[0] = 6
    print(tu_ple)
except:
    print("Error occured")

try:
    li_st[0] = 6
    print(li_st)
except:
    print("Error occured")

#answer - <class 'tuple'>
#         <class 'list'> 
#According to this example, it shows that tuples are immutable and list are mutable.

# (7) Create a function that grabs the email website domain from a string in the form:
# user@domain.com 
# So for example, passing "user@domain.com" would return: domain.com
email = input("Enter an email: ")
c = 0
found = True
n = len(email)
while(c<n):
    if(email[c]=='@'):
        print(email[c+1:])
        found = False
    c = c+1
if(found):
   print("It is not an email.")

# (8) Create a basic function that returns True if the word 'dog' is contained in the input string. 
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
str = input("Enter string: ")
str = str.lower()

def func(param):
    return 'dog' in param

print(func(str))

#(9) Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases
str = input("Enter string: ")
str = str.lower()

def func(param):
    return param.count("dog")

print(func(str))

# (10) Use lambda expressions and the filter() function to filter out words from a list that don't start with 
# the letter 's'. For example:
# seq = ['soup','dog','salad','cat','great']
# should be filtered down to: ['soup','salad']
arr = []
i = 0

while i<5:
    lst = input("Enter word/string:")
    arr.append(lst)
    i = i+1

print(list(filter(lambda num: num[0] != 's',arr)))

# (11) You are driving a little too fast, and a police officer stops you. Write a function to return 
# one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, 
# the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, 
# the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) 
# -- on your birthday, your speed can be 5 higher in all cases.
num = int(input("Enter speed: "))
bday  = input("Is your birthday(T/F): ")
bday.lower()
if bday=='t':
    bday = True
else:
    bday = False

def func(speed,bday):
    if bday:
        speed = speed-5
    if(speed <= 60):
        print("No Ticket")
    elif(speed>=61 and speed<=80):
        print("Small Ticket")
    else:
        print("Big Ticket")

func(num,bday)






































