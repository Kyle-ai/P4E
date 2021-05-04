#Prompt the user for rate of pay and hours to compute gross pay.
rate = input("Enter rate of pay: ")
hours = input("Enter hours:" )
fhours = float(hours)
frate = float(rate)
computepay = frate * fhours
print(computepay)
