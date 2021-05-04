#Write a program to to prompt a user for celsius, convert to farenheight print
#converted tempeture. formula = (0°C × 9/5) + 32 = 32°F
def tempConverter():
    celsius = input()
    temp = int(celsius)
    f = (temp * 9/5) + 32
    print(f)

tempConverter()
