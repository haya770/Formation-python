
#question 1
def IsPos(a= None):
    num = int(input("rentrez un chiffre"))
    
    if num>0 :
        return  "positif"
    elif num<0 :
        return "negatif"
    else :
      0



#question 2

def IsLeapYear():

    try:
        year = int(input("entre une annee "))
        if year %4 ==0:
            print("annéee bissextile")
        else:
            print("pasa annee bix")

    except ValueError:
        print("erreur")

print(IsLeapYear())
