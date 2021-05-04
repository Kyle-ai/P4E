#Write a program that reads a file and prints the letters in decreasing order of
#frequency. Your program should convert all the input to lower case and only
#count the letters a-z.Your program should not count spaces, digits, or
#punctuation. Find txt samples from several diffrent languages and
#see how letter frequency varies between languages.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
fname = input('Enter file name: ')   #use romeo.txt
fhandle = open(fname)
text = fhandle.read()
freq_dict = {}
for char in text.lower():
    if char in alphabet:
        freq_dict[char] = freq_dict.get(char, 0) + 1
#print(freq_dict)
freq = []

for key, value in freq_dict.items():
    freq.append((value, key))
freq.sort(reverse = True)
print(freq)
