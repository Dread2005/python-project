####### How To Read In a File ##########
#file = open("the_other_file.txt")
#content = file.read()
#print(content)
#always close the file when you are done
#file.close()
# if you would rather leave file.close alone, use the with keyword
#with open("the_other_file.txt") as file:
#    content = file.read()
#    print(content)

####### How To Write In a File ##########
#change the mode to write(w)
#to add to the written text, use mode(a) [for append]
#with open("the_other_file.txt", "a") as file:
 #   file.write("\n we are the champions my froe")

### if a file doesn't exist in write mode: it will create it from scratch
#ONLY WORKS IN WRITE
#with open("the_other_other_file.txt", "a") as file:
 #   file.write("\n we are kings")

#### Paths In Python ####
#we  deal with files and folders
# files can be in folders
# you csn have multiple folders inside each other
# the Root is the origin, the main folder, the c: Drive

######Absolute File Path#########
# to get a file using Absolute File Path c:/ Work(folder)/Project(folder)/talk.ppt(file)

######Relative File Path#########
#working directory(the folder you're working on)
#this is from the file you're working in
#./talk.ppt
#this one is from the file outside the working file
#./Project/talk.ppt
#to go up in the directory


####Absolute#####
with open("/Users/Tshifhiwa/Documents/the_other_file.txt") as file:
    print(file)

####Relativee#####
with open("../../../Documents/the_other_file.txt") as file:
    files = file.read()
    print(files)







