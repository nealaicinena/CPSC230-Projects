print("PASSWORD CRITERIA")
print("_________________________________")
print("-Must be 8 characters or more")
print("-Must contain 1 uppercase letter")
print("-Must contain 3 numbers")
print("-Must contain the word cat")
print("-Must contain 1 question mark (?)")
print("No spaces allowed")
print("_________________________________")
password = input("Please create a password: ") #asks for a password
#tells the user all the criteria for the password

passwordWorks = False
password8Chars = False
password1Upper = False
password3Nums = False
passwordCat = False
passwordQMark = False
passwordNoSpace = False
#defines all the variables as false before it checks the password if each criteria is true

while(passwordWorks == False): #while password is false, loop will keep checking for each critiera
    if(len(password) < 8): #checks if password is too short
        password8Chars = False
        print("Password must be at least 8 characters") #tells the user this criteria isn't met
    else:
         password8Chars = True #if its long enough, this criteria is set to true
    if(password.islower() == True): #checks if the whole password is lowercase AKA is missing an uppercase letter
        password1Upper = False
        print("Password must have at least 1 upper case character")
    else:
        password1Upper = True #if there is an upper case then this criteria is set to true
    nums = 0 #starts a number counter for total numbers in the string
    if(password3Nums == False):
        for i in range(len(password)): #checks every character of the string
            if(password[i].isdigit()): #if the character is a digit then 1 is added to nums
                nums += 1
        if(nums < 3): #if nums is not big enough then tells the user this criteria is not met
                print("Password must have at least 3 numbers")
        else:
             password3Nums = True #if there are 3 or more numbers then this critera is set to true 
    if("cat" not in password): #checks if the word "cat" is in the password
        passwordCat = False
        print("Password must contain the word cat at least once")
    else:
        passwordCat = True #if "cat" is in the password then this critera is set to true
    if("?" not in password): #checks if there is a question mark in the password
        passwordQMark = False
        print("Password must contain at least 1 question mark")
    else: #if there is a question mark, this criteria is set as true
        passwordQMark = True
    if(" " in password): #checks if there is a space
        passwordSpace = False
        print("Password cannot contain any spaces")
    else:
        passwordSpace = True #if there are no spaces, this criteria is set to true
    if(password8Chars == True and password1Upper == True and password3Nums == True and passwordCat == True and passwordQMark == True and passwordSpace == True): #if all the criteria is met, the password works and is set as true
        print("Sucess!")
        print("Password meets all criteria!")
        passwordWorks = True #sets passwordWorks to true so that the while loop ends
    else: #asks the user to give a new password so it can run the while loop again and check the criteria
        password = input("Please enter a new password that fits this criteria: ")
    
