somme =0
for i in range(0,101):
    if i%3==0 and i%5==0:
        somme = somme+i
print(somme)

#question 2

def IsPrem(a):
    somme = 0
    for i in range(2,a):
       
        if a%i==0:
            somme = somme +1
    if somme ==0:
        return True
    else :
        return False





IsPrem(13)
IsPrem(12)

#exercice 3
def IsListEqu(list1,list2):
    list3=[]
    
    for i in list1:
        for j in list2:
            if i==j:
                list3.append(i)

    print(list3)

c=[4,2,7,8,5,6,2,3]
d=[1,3,2,18,6,4]
IsListEqu(c,d)


#question 4


#question 5 

IsPrem(13)
IsPrem(12)

list2=[]
for i in range(0,100):

    if IsPrem(i)==1:
        list2.append(i)
print(list2)