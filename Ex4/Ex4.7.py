#Rewrite the grade program from the previous chapter usiung a function called
#computegrade that takes a score as its paracode and returns a grade as a string
initialscore = input("Please enter score:")
score = float(initialscore)
def computegrade(score):
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
computegrade(score)
