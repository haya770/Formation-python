#Question 1
list = "a a bb c aa a a "

mot_sep = list.split()

#dictionnaries

freq = {}

for i in mot_sep:
    if i in freq:
        freq[i] = freq[i]+1
    else:
        freq[i] = 1

print(freq)
print(mot_sep)

#creation d'un dictionnaire

note ={'math':15, 'francais':14, 'histoire': 13 }
note['anglais'] =16
print(note)
note['math']=18
print(note)


print(note.items())
print(note.keys())

for i, j in note.items():
    print (f"{i}:{j}")
somme = 0
n = 0
for i ,j in note.items():
    j
    somme = somme+j
    n =n +1
print(sum(note.values())/len(note.items()))
print (somme/n)


#exercice 2

a = {'math':14, 'anglais':16,'histoire':13}
b = {'francais':14, 'anglais':16,'histoire':13}
m = {}
for i, j in a.items():
    for c,d in b.items():
        if i==c and j==d:
            m[f"{i}"]= j
print (m)