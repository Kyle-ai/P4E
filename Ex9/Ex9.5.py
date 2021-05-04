#This program records the domain name (instead of the adress) where the message
#was sent from instead of who the mail came from(i.e. the whole email adress).
#At the end of the program, print out the contents of your dictionary.
fname = input('Enter file name: ')
doms = dict()
try:
    fhandle = open(fname)
except:
    print('Invalid file entered: ', fname)
for line in fhandle:
    if line.startswith('From '):
        atpos = line.find('@')
        npos = line[atpos + 1:]
        dom = npos.split()[0]
        doms[dom] = doms.get(dom,0) + 1

max_num = 0
max_dom = None
for key in doms:
    if doms[key] > max_num:
        max_dom = key
        max_num = doms[key]
print(max_num, max_dom)
# result = 8 iupui.edu
