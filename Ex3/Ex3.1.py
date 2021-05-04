#Rewrite your paycomputation to give the employee 1.5 times the hourly rate for
#hours wortkedf from above 40.
rate = input("Enter rate of pay: ")
hours = input("Enter hours:" )
fhours = float(hours)
frate = float(rate)
if fhours > 40:
    reg = fhours * frate
    otp = (fhours - 40) * 1.5
    total = otp + reg
    print(total, otp)
else:
    total = frate * fhours
    print(total)
