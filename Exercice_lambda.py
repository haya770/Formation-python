# 1- Write a lambda function that adds 15 to a given number. 
# (15 --> 30)

ajout_quinz = lambda x : x+15

print(ajout_quinz(20))


# 2- Write a lambda function that multiplies argument x with argument y and.
# (4, 6 --> 24)
multiplies = lambda x,y: x*y
print(multiplies(6,4))



# 3- create a list of tuples where each tuple contains name and grade. sort the list by the grades
# ( [('itai', 88),  ('amit', 97), ('maayan', 90)] -->  [('amit', 97), ('maayan', 90), ('itai', 88)] )

student = [('itai', 88),  ('amit', 97), ('maayan', 90)] 

sorted_student = sorted(student,key = lambda x: x[1],reverse=True)
print(sorted_student)

#3 bis ajoute 5 a chaque note

student_plus_cinq = list(map(lambda x: (x[0], x[1]+5), student))
print (student_plus_cinq)
#map(fonction, iteration)
# 4- create a list of dictionaries of cars containing the keys: model, year, color. sort the list by color.(use the function sorted)
# ( [{model: hyundai, year: 2020, color: red}, {model: mitsubishi, year: 2019, color: black}, {model: hyundai, year: 2021, color: blue}] -->
# [{model: mitsubishi, year: 2019, color: black}, {model: hyundai, year: 2021, color: blue}, {model: hyundai, year: 2020, color: red}]  )

# 5- create 2 lamda filters both recive a list of numbers one returns even numbers the other odds.
nombre = [1,2,3,4,5,6,7,8]
even = list(filter(lambda x:(x%2==0),nombre))
odd = list(filter(lambda x:(x%2!=0),nombre))
print(odd)
#Fonction	Rôle principal	Ce qu'elle retourne
#map()	Transforme chaque élément	Une nouvelle liste transformée
#filter()	Garde seulement certains éléments

# 6- create a lambda function that recive a list of numbers and return all the numbers squered	
list_squerred = list( map(lambda x:(x**0.5),nombre))
print(list_squerred)