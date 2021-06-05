string1 = "my name is Rupsha           "
string2 = "Rupsha"
string3 = "This is fully, and wholly; different"

#substring match:
print (string2 in string1)

#string slicing: 
print(string1.split(" "))
print(string3.split(','))

#whitespace trimming:
print(string1.strip()+string2)

#extract substring: perform action on the string ad if it's a list
