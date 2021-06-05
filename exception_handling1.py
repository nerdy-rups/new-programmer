## Method 1 -- using forced exceptions

ItemUnderTest = 10

if ItemUnderTest != 10:
    # raise Exception("Test failed. count does not match")
    pass # <----- a keyword to let that portion of the condition skip

#assert(ItemUnderTest == 20)



## Method 2 -- using try-except 

try:
    with open('testfile.txt', 'r') as filereader:
        filereader.read()
except:
    print("Hii, i am an error" , Exception)
