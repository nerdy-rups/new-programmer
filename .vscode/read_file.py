# open the test1.txt file and read all it's contents 

#Using readline method
Myfile = open("test1.txt")
lineFromFile = Myfile.readline()
print (lineFromFile)
while lineFromFile != '':
    print(lineFromFile, end = '')
    lineFromFile = Myfile.readline()

print ('****************************************************************************************************************************')

#using readlines method
MyfileAgain = open("test1.txt")
allContent = MyfileAgain.readlines()
print(allContent)
for item in allContent:
    print(item)


MyfileAgain.close()
