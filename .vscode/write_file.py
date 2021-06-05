#open the test2.txt file in read mode --> read all contents --> reverse the order of the contents --> edit the original file to store this reversed content. 


with open("test2.txt", "r") as fileReader:  # with open() method removes the need to explicity close the file after completing execution. 
    fileContent = fileReader.readlines()
    with open("test2.txt", "w") as fileWriter:
        for line in reversed(fileContent):  #reversed method reverses a list
            fileWriter.write(line)