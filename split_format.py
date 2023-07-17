#split method: This method will split the string into list of words with the help of given separator.
#providing separator is not mandatory ,it takes default value as space.
s = 'engineering'
print(s.split('e'))
print(s.split('g'))
print(s.split('er'))
print(s.split('ng'))

#Format String: This method is used to insert values in a string with the help of place holder({})
name = 'Ram'
marks = 75
sub = 'English'
print('{} scored {} marks in {}'.format(name,marks,sub))
print('{2} scored {0} marks in {1}'.format(marks,sub,name))
print('{n} scored {m} marks in {s}'.format(m=marks,s=sub,n=name))



