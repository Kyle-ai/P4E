#rerite your pay computation with time and a half for over time and create a
#function called computepay which takes two parameters(hours and rate
hours = input("Enter hours:")
rate = input("Enter pay:")

def computepay(hours,rate):
    try:
        fhours = float(hours)
        frate = float(rate)
    except:
        print("Please enter valid input")
    if fhours > 40:
        reg = fhours * frate
        otp = (fhours - 40) * 1.5
        total = otp + reg
        print(total)
    else:
        total = frate * fhours
        print(total)

computepay(hours,rate)
