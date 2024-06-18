#asks the user to input the price of an item and stores it as price
price = float(input("please enter the price of an item: "))

#checks to make sure price is not negative before continuing
#the computation does not run if price is negative
if(price >= 0):
    #asks the user to input the tax of the same item and stores it as tax
    tax= float(input("please enter the tax for the item: "))

    #checks to make sure tax is not negative before continuing
    #the computation does not run if tax is negative
    if(tax >= 0):
        #takes tax and converts it so that it can be multiplied by price to get total price
        tax = (tax/100) + 1

        #calculates total price by multiplying price and tax
        totalPrice = price * tax

        #prints to the user the total price of the item given the price and the tax
        print("the total price of that item with tax is", totalPrice)
    else:
        #tells the user that tax cannot be negative
        print("invalid input")
        print("input cannot be negative")
else:
    #tells the user that price cannot be negative
    print("invalid input")
    print("input cannot be negative")