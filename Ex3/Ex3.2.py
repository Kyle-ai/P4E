#Rewrite the paycomputaion using try and except so that your program handles
#nonenumeric input gracefully
#by printing a message and exiting the program.

rate = input("Enter rate of pay: ")
hours = input("Enter hours:" )
fhours = float(hours)
frate = float(rate)
try:
    if fhours > 40:
        reg = fhours * frate
        otp = (fhours - 40) * 1.5
        total = otp + reg
        print(total, otp)
except:
    print("Invalid")
    else:
    total = frate * fhours
    print(total)
