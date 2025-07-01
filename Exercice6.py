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