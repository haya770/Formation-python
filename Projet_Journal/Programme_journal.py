# etape 1ret
import os 
import datetime

#voir si mon dossier journal existe

def Existe(Journal):
    if os.path.exists(Journal):
       return 1
    else :
        os.makedirs(Journal)
    
print(Existe("Journal2"))

def ma_fonction():
    print("Bonjour")

if __name__ == "__main__":
    ma_fonction()

#1. faire un menu avec 5 choix
# 1 crerer lire modifier suprimer quitter
# 
def creer(fichier):
    if os.path.exists("Journal"):
        if os.path.exists(fichier):
            with open(fichier,"+a") as file:
                file.write ("creation de contenu")
        else:
             with open(fichier,"w") as file:
                file.write ("creation de contenu")

                
            

if __name__==   '__main__':
    creer("text1.txt")
