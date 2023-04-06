#Here we will learn about regular expression in Python. It is used for pattern matching. There are functions: 


# Meta Characters
# [] A set of characters
# \ Signals a special sequence (can also be used to escape special characters)
# . Any character (except newline character)
# ^ Starts with
# $ Ends with
# * Zero or more occurrences
# + One or more occurrences
# {} Exactly the specified number of occurrences
# | Either or
# () Capture and group
# Special Sequences
# \A Returns a match if the specified characters are at the beginning of the string
# \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

# \d Returns a match where the string contains digits (numbers from 0-9)
# \D Returns a match where the string DOES NOT contain digits
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character
# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \W Returns a match where the string DOES NOT contain any word characters
# \Z Returns a match if the specified characters are at the end of the string
import re
mystr="Hard work never goes in vain.I am a hard worker.hhhaaqa"
patt= re.compile(r'Hard')
matches=patt.finditer(mystr)
for match in matches:
    print(match) # match is a regex object which will contaon span , match
    print(mystr[0:4]) # here 0 and 4 came from span.span in regex shows the staring and ending index of of Hard in string mystr

# patt=re.compile(r'.') It is used to match any character
#Now we want to serarch that staring mne koi bhi character ho and baad me 'work' ho
patt=re.compile(r'.work')
matches=patt.finditer(mystr)
for match in matches:
    print(match) # match is a regex object which will contaon span , match

patt=re.compile(r'^Hard')
matches=patt.finditer(mystr)
for match in matches:
    print(match)    
patt=re.compile(r'worker$')
matches=patt.finditer(mystr)
for match in matches:
    print(match)    
    #Now there should be 'h' and zero or more occrences of 'a'

patt=re.compile(r'ha*')
matches=patt.finditer(mystr)
for match in matches:
    print(match)    

print("******")    
#To find exact no. of oocurences
patt=re.compile(r'a{2}')
matches=patt.finditer(mystr)
for match in matches:
    print(match)    

print("******")    
#To find combination of exact no. of oocurences
patt=re.compile(r'(ha){1}')
matches=patt.finditer(mystr)
for match in matches:
    print(match)    

print("******")    
#To perform either or. either I will get 2 'a' or worker
patt=re.compile(r'a{2}|worker')
matches=patt.finditer(mystr)
for match in matches:
    print(match)    

#Now there are some special sequencxes also like \A, \b, \B, \d,\D,,\s,\S,\w,\W,\Z
mystr="34567-7948 and here"

print("******")    
#To  search 5 digits and then a dash and then 4 digits
patt=re.compile(r'\d{5}-\d{4}')
matches=patt.finditer(mystr)
for match in matches:
    print(match)    

mystr="+91 6655483493, +91 2323232323 , 84934839"
print("******")    
#To get all the numbers that start with +91 and then contain 10 digits
patt=re.compile(r'\+91 \d{10}')
matches=patt.finditer(mystr)
for match in matches:
    print(match)    



