#input values of A, B, and C for the quadratic formula.
import math
A = input("A value: ")
B = input("B value: ")
C = input("C value: ")


#I'll just use the discriminant, because that's easier.
D = ((B**2)-(4*A*C))


if D <= 0: #if the discriminant is less than 0 the answer is imaginary
    DTwo = (math.sqrt(math.fabs(D))) / float((2 * A)) #square root of the absolute
    #value of the discriminant divided by 2A

    NegBOverTwoA = ((B - (2 * B)) / float(A + A))
    
    if DTwo <= 0: #incorporating addition or subtraction
        Sign = str("-")
    else:
        Sign = str("+")
    DTwo = str(DTwo)
    DTwo = str(DTwo + "i")
    NegBOverTwoA = str(NegBOverTwoA)
    FirstAnswer = str(NegBOverTwoA + Sign + DTwo)
    FirstAnswer = str(NegBOverTwoA + Sign + DTwo) #since the first answer is the
    #possibility that the discriminant is added to -b we need no sign change
    print FirstAnswer
    
    #switching signs for SecondAnswer since it's -b minus the discriminant
    if Sign == "-":
        Sign = "+"
    else:
        Sign = "-"
        
    SecondAnswer = str(NegBOverTwoA + Sign + DTwo)
    print SecondAnswer
    
else: #If the discriminant is not negative in the first place, then there is
#no reason to do that insanity of trying to make Python understand imaginary
#numbers at least a little better.... XD
    FirstAnswer = (-B + (math.sqrt(D))) / float(2 * A)
    print FirstAnswer
    SecondAnswer = (-B - (math.sqrt(D))) / float(2 * A)
    print SecondAnswer