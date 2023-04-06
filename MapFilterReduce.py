#Firstly we will see about filter. filter will take a list and will filter the lsit according to our requirement.We will ask 
# filter that whether the number present in the list is even or not. First argument will be function that will be executed for 
# each  item of the list and second argument will be the list
from functools import reduce
my_lst=[2,3,5,6,7]
evens=list(filter(lambda n: n%2==0,my_lst))
print(evens)
#If you have bunch of values ,filter those values that you don't need and apply some operations with the help of map such as 
# adding +2 to all the even numbers and after that if you want to add all the values returned by map,then you can use reduce.
#But remember one thing that to use reduce function you have to import reduce from functools 
doubles=list(map(lambda n:n*2,evens))
print(doubles)
sum=reduce(lambda a,b: a+b,doubles)
print(sum)