#question 1
#ok
#question 2
with open("data.txt", "r") as file:
    contenu = file.read()
    print(contenu)

try:
    with open("re.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")


file =open("data.txt","w")
file.write ("Helo")
file.close()

contenu =open("data.txt","r").read()
print(contenu)
file.close()


#question 
try:
    result = 10/0
except ZeroDivisionError:
    print("erreur")

#question 8
#"\n" va a la ligne
with open("data.txt", "a+") as file:
    file.write("saly \n")
file.close()

with open("data.txt", "r") as file:
     contenu =file.read()
print(contenu)


#question 12

def safe_divide(a,b):
    
    try:
        return a/b


    except ZeroDivisionError:
        return ("cant divisie")

print(safe_divide(5,6))


try:
    num = int(input("Entrez un nombre entier : "))
except ValueError:
    print("Value error occurred")
else:
    print("No error occurred")


