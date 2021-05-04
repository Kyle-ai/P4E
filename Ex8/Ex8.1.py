#Write a function called chop that takes a list and modifies it, removing the
#frst and last elements, and reutrns None. Then write a function called
#middle that takes a list and returns a new list that contains all but
#the first and last elements.

def chop(t):
    del t[0],t[-1]         #modifies the original lst
lst = [1,2,3,4,5]
chop(lst)
print(lst)
output[2,3,4]

def middle(t):
    return t[1:-1]        #does not modify the original but returns a new lst
newlst = middle(lst)
print(newlst)
