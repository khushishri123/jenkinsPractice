def genSquares():
    n=1
    while n<=10:
        sq=n*n
        # Now we will make use of yield keyword to make this function as generator.There is a difference between 
        # yield and return statement.Return statement will treminate the function but yield does not. It is an alternative for 
        # iterator.
        yield sq
        n=n+1

values=genSquares()
print(values)
#Now to extract the sqaures from values,extracting first value:
#print(values.__next__())
#also we can use a loop to extract rest of the values:
for i in values:
    print(i)
