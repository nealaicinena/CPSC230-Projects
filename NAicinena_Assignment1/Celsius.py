#ask the user for a temperature in celsius and store it as a float in celsius
celsius = float(input(("please enter a temperature in Celsius:")))

#convert celsius to fahrenheit and store it in fahren
fahren = (celsius * (9/5)) + 32

#prints to the user the inputed temperature converted to fahrenheit
print("that temperature in celsius is", fahren)