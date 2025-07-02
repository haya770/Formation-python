#question 1

strings = ['foo', 'bar', 'baz']  


strings_prem = [ i[0] for i in strings]
print(strings_prem)


#question 2

nums = [2,3,4,5]

nums_carre = [i**2 for i in nums]
print(nums_carre)

#question 3

nums = [1,2,3,4,5,6,7,8]  
def filter_even(liste):
    nums_even = [i  for i in nums if i%2==0]
    print(nums_even)

filter_even(nums)

#question 4
list1 = [1,2,3] 
list2 = [4,5,6] 

list3 = list1+list2
print(list3)

#question 1

strings = ['foo', 'bar', 'baz']  
str2 = [i[0] for i in strings]
print (str2)

#question 2
nbr =[2,4,6,8,10]
nbr_carre = [i*i for i in nbr]
print(nbr_carre)

#question 3
nbr =[1,2,3,4,5,6]
nbr_pair = [i for i in nbr if i%2==0]
print(nbr_pair)

#question 4
list1 = [1,2,3] 
list2 = [4,5,6] 
list3 = list1+list2
print(list3)

#question 5 
strings = ['foo', 'bar', 'baz','Messi']
keys = [len(i) for i in strings]

m_dict ={}
for s,k in zip(strings,keys):
    m_dict[s]=k
strings = ['foo', 'bar', 'baz','Messi']
keys = [len(i) for i in strings]
for s,k in zip(strings,keys):
    if k not in m_dict:
       m_dict[k]=[]
    m_dict[k].append(s)
    
    
print(m_dict)

strings = ['foo', 'bar', 'baz']  
cpt = 0
for i in strings:
    
   
    if 'a' in i:

        cpt =cpt+1
print(cpt)