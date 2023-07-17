#INDEX METHOD: This method returns index position of first occurance of given substring.
#if substring is not part of the string it return value error.
s = 'we are what we are'
print(s.index('are'))
print(s.index('what'))
print(s.index('we'))

#r.index method: It returns the position of last position of last occurance of given substring.
#if substring is not present in the given string then, it return the value error.

print(s.rindex('we'))
print(s.rindex('what'))
print(s.rindex('are'))

#FIND METHOD: It returns index position of first occurence of given substring.
#if substring is not part of the string,it returns '-1'
print(s.find('a',3,10))
print(s.find('w',2,11))
print(s.find('w'))
print(s.find('c'))
#rfind method: It returns index position of last position of last occurance of given substring.
#if substring is not of the string,it returns '-1'

print(s.rfind('a',3,10))
print(s.rfind('w',2,11))
print(s.rfind('w'))
print(s.rfind('c'))





