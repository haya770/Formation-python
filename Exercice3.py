
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


#question 3

def IsOdd(number):
    if number%2==0:
        print ("pair")
    else:
        print("impair")

IsOdd(5)


#question 4 

def PlusGrand(a, b, c):
    return (max(a,b,c))
print(PlusGrand(4,4,6))

#exercice 5
def IsVoyelle(e):
    if e in ('a','u','e','i','o','y'):
        return ("voyelle")
    else:
        return ("cons")
    
print (IsVoyelle('b'))
print (IsVoyelle('a'))

#exercice 6
def IsPalindrome(word):
    word = list(word)
    word2 = word [::-1]
    somme=0
    if word ==word2:
        print("palindromme")
    else :
        print("no pal")

IsPalindrome('madam')

#Exercice 7,8 ok

#exercice 9 

def IsSquare(num):
    num2 = num**0.5 
    if num2.is_integer():
        return ("yes")
    else :
        return ("no")
    
print (IsSquare(14))
print (IsSquare(16))

#exercice 10
#ok


