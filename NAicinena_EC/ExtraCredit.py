from math import factorial
from datetime import date, datetime, timedelta
#Python Basics and Math Operations
#--------------------------------------------------------------------------------------------------
print("Please enter your birthday (MM,DD,YYYY) separated by commas")#asks user for their birthday
dateOfBirth = input("Please do not add extra zeros: ")
dOfBSplit = dateOfBirth.split(",")#makes list of month, day, and year
dOfBSplit[0] = int(dOfBSplit[0])#turns each element into an int
dOfBSplit[1] = int(dOfBSplit[1])
dOfBSplit[2] = int(dOfBSplit[2])

date1 = datetime(dOfBSplit[2], dOfBSplit[0], dOfBSplit[1])#creates two dates
date2 = datetime(2022,11,28)#one for the birthday and one for today

print("Your age in days is ", (date2 - date1))#tells the user the difference in days
#--------------------------------------------------------------------------------------------------
#Conditionals #1
military = input("Please enter a time in military time and I will convert it to 12 hour format time: ")#asks user for 24 hr format time
regular = 0 #sets regular time to 0
amPm = "am" #creates am/pm
try: #tries to make the conversion
    military = int(military)
    if(0 <= military < 13):
        if(military == 0): #if it is midnight then regular is 12 am
            regular = 12
        else:
            regular = military #otherwise regular is the same as military
        if(military == 12):
            amPm = "pm" #if it is noon then regular becomes pm not am
        else:
            amPm = "am" #otherwise make it morning
        print(regular, amPm)#tells the user the new time
    elif(12 < military < 24): #if it is in the afternoon then subract 12 from the military
        regular = military - 12
        amPm = "pm" #and sets it to pm
        print(regular, amPm) #tells the user the new time
    else:
        print("Invalid input")#if number is not between 0 and 23
except: #if there is an error it says invalid
    print("Invalid input")
#--------------------------------------------------------------------------------------------------
#Conditionals #2
userInput = input("Please enter 2 integers separated by a comma (,): ")#asks the user for 2 numbers
userNumbers = userInput.split(",")#splits and makes it a list
userNumbers[0] = int(userNumbers[0]) #converts elements to a list
userNumbers[1] = int(userNumbers[1]) #converts elements to a list
addOrMult = int(input("Do you wish to add [1] or multiply [2] these 2 numbers? (Press 1 or 2): "))#if 1 then add, if 2 then multiply

if(addOrMult == 1):
    print("sum:", userNumbers[0] + userNumbers[1]) #prints the sum
elif(addOrMult == 2):
    print("product:", userNumbers[0] * userNumbers[1]) #prints the product

if(userNumbers[0] == userNumbers[1]): 
    print("Same")#if the numbers are the same print same
else:
    print("Different")#if the numbers are different print different

#--------------------------------------------------------------------------------------------------
#Conditionals #3
userInput = input("Please enter your height (in inches) and your weight (in pounds) to calculate your BMI (separate by a comma): ")#asks for height and weight
measurements = userInput.split(",")#separates height and weight in list
measurements[0] = float(measurements[0])#converts both to floats
measurements[1] = float(measurements[1])#converts both to floats

bmi = (measurements[1]/(measurements[0] ** 2)) * 703 #calculates the bmi

weightStatus = "" #creates weight status
if(bmi < 18.5): #overweight if bmi under 18.5
    weightStatus = "underweight"
elif(18.5 <= bmi < 25): #normal if bmi over 18.5
    weightStatus = "normal"
elif(25 <= bmi < 30): #overweight if bmi over 25
    weightStatus = "overweight"
elif(bmi >= 30): #obese if bmi over 30
    weightStatus = "obese"

print("Your BMI is", bmi, "and you are considered", weightStatus) #tells the user bmi and their weight status
#--------------------------------------------------------------------------------------------------
#Strings #1
num = 0 #sets num to 0
divis10 = [] #creates empty list
while len(divis10) < 10: #while list is less than 10 elements
    num += 1 #iterates num
    if(num % 3 == 0): #if divisible by 3
        divis10.append(num) #add num to the list
print("The first 10 numbers divisible by 3 starting at 0: ", divis10)#print all the nums
#--------------------------------------------------------------------------------------------------
#Strings #2
userInput = input("Please enter 2 numbers separated by a comma: ")#ask the user for 2 numbers
nums = userInput.split(",")#creates list of 2 numbers
nums[0] = int(nums[0])#makes both elements ints
nums[1] = int(nums[1])#makes both elements ints
print(nums[0] + nums[1]) #prints the sum
tries = 0 #tries is 0
while((nums[0] + nums[1]) == 0 and tries < 2): #if the tries is less than 2 and the sum is 0
    tries += 1 #add another try
    print("Your sum was equal to 0 so you get to do it again")
    userInput = input("Please enter 2 numbers separated by a comma: ")#asks user for 2 numbers again
    nums = userInput.split(",")#separates numbers in a list
    nums[0] = int(nums[0])#makes them both ints
    nums[1] = int(nums[1])
    print(nums[0] + nums[1])#prints sum
print("goodbye")#says goodbye
#--------------------------------------------------------------------------------------------------
#Strings #3
letter = input("Please enter a lowercase letter: ")#asks for a lowercase letter
print("Every letter from", letter, "to the end of the alphabet is as follows: ")
while(letter < "{"):#while letter index is less than index of {
    print(letter)#prints the letter
    letter = chr(ord(letter) + 1)#increases letter index
#--------------------------------------------------------------------------------------------------
#Strings #4
userInput = input("Please enter a string: ")#asks user for a string

vowels = 0#vowels is 0
for i in userInput: #iterates all characters of the string
    if(i in "aeiou"):#if i is a vowel
        vowels += 1#add 1 to vowel
if(vowels >= 3):#if vowels is greater than 3
    print("vowel heavy!")#print vowel heavy
else:
    print("consonant heavy!")#print consonant heavy
#--------------------------------------------------------------------------------------------------
#Functions #1
def reverse(string1):
    string1 = string1.upper()#makes the string uppercase
    string1 = string1[::-1]#makes the string the reverse of the string
    return string1

userInput = input("Please enter a string to be reversed and capitalized: ")#asks user for a string
print(reverse(userInput))#returns the capitalized and reverse version of the string

#--------------------------------------------------------------------------------------------------
#Functions #2
def factorial(num): #uses recursion to call the fuction and keep multiplying by one less than the number till it gets to 1
    if(num > 1):#if the number is more than 1
        return num * factorial(num - 1)#multiply by num-1 in factorial
    else:
        return num#returns total factorial

userInput = int(input("Please enter a number: "))#asks the user for a number
print("factorial of", userInput, "is", factorial(userInput))#puts user input in the factorial
#--------------------------------------------------------------------------------------------------
#Functions #3
def minimum(num1, num2, num3):
    nums = [num1, num2, num3]#creates list of the numbers
    return min(nums)#returns smallest of the list

userInput = input("Please enter 3 numbers separated by a comma: ")#asks user for 3 numbers separated by a comma
nums = userInput.split(",")#creates list of separated elements
nums[0] = int(nums[0])#converts all elements to ints
nums[1] = int(nums[1])
nums[2] = int(nums[2])
print(minimum(nums[0], nums[1], nums[2]))#puts all 3 elements into minimum function

#--------------------------------------------------------------------------------------------------
#Functions #4
def counter(string1):
    upper = 0
    lower = 0
    for i in string1:#goes through each character of the string
        if(i.isupper()):#if the character is upper
            upper += 1#add one to the upper
        elif(i.islower()):#if the character is lower
            lower += 1#add one to lower
    print("Uppercase letters: ", upper, "Lowercase letters:", lower)#print all the upper and lower totals

userInput = input("Please enter a string: ")#ask the user for a string
counter(userInput)#puts the input into counter
#--------------------------------------------------------------------------------------------------
#Functions #5
def a():
    return "hello"#function returns hello
def b():
    return "world"#function returns world
def c():
    return (a() + " " + b())#function returns functions a and b

print(c())#prints function c
#--------------------------------------------------------------------------------------------------
#Lists #1
userInput = input("Please enter a string: ")#asks the user for a string
list1 = []#creates empty list
for i in userInput:#iterates each character in string
    list1.append(i)#adds character to the list

print(list1)#prints the list
#--------------------------------------------------------------------------------------------------
#Lists #2
userInput = input("Please enter a string of numbers: ")#asks the user for a string of numbers
sum = 0#sets sum to 0
product = 1#sets product to 1
for i in userInput:#iterates each number in the string
    i = int(i)#makes the string a number
    sum += i#add number to the sum
    product *= i#multiply product by the number
print("The sum of all those numbers is", sum, "The product of all those numbers is", product)#print the sum and product
#--------------------------------------------------------------------------------------------------
#Lists #3
list1 = []#creates empty list
for i in range(100):#iterates each number from 0 to 100
    if(i % 7 == 0):#if number is divisible by 7
        list1.append(i)#adds number to the list

print("Every number divisible by 7 from 0 to 100: ", list1)#prints the list
#--------------------------------------------------------------------------------------------------
#Lists #4
list_A = [1,2,3,4,5,6]#creates the 2 lists
list_B = [4,5,6,7,8]

print("All the numbers that are the same in list A and B are as follows: ")
for i in list_A:#go through each element of list A
    for j in list_B:#go through each element of list B
        if(i == j): #if the elements are the same print it
            print(i)
#--------------------------------------------------------------------------------------------------
#Lists #5
list_A = [1,2,3,4,5,6]#creates list A
list_B = []#creates empty list B
for i in list_A: #goes through each element of A
    list_B.insert(i, len(list_A) - list_A.index(i))#adds each element to the opposite index of list A into list B

print("List A reversed is ", list_B)#print the reversed list
#--------------------------------------------------------------------------------------------------
#Lists #6
rows = int(input("Please enter how many rows of Pascal's Triangle you want: "))#asks the user for how many rows they want

for i in range(rows):#iterates from 0 to the user input
    for j in range(rows - i + 1):#iterates from user input minus i plus 1
        print(end = " ")#prints a space
    for j in range(i + 1):#iterates from 0 to i + 1
        print((factorial(i) // (factorial(j) * factorial(i - j))), end = " ") # calcuates the number that needs to be printed
    print()#print empty string and go to a new string