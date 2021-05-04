#Take the python code in str = 'X-DSPAM-Confidence:0.8475'
#use find and string slicing to extract the portion of the string after the
#colon charecter. Then use float() to  convert the string to a flaoting point.

str = 'X-DSPAM-Confidence:0.8475'
apos = str.find(':')
newpos = float(str[apos +1:])
print(newpos)
