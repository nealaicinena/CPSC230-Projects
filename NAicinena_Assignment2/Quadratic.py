from math import sqrt

#asks the user to input coefficients of a quadratic equation and stores them as variables
a = float(input("please enter first coefficient of quadratic: "))
b = float(input("please enter second coefficient of quadratic: "))
c = float(input("please enter third coefficient of quadratic: "))

#calculates the discriminate and stores it as variable d
d = (b ** 2) - (4 * a * c)

if(d >= 0):
    #computes the first and second roots of the quadratic using the input from the user 
    root1 = (-b - sqrt(d)) / (2 * a)
    root2 = (-b + sqrt(d)) / (2 * a)

    #prints to the user both the roots or prints the same one twice if there is one root
    print(root1, ",", root2)
else:
    #tells the user that there are no roots because the descriminate is negative
    print("there are no roots that exist")