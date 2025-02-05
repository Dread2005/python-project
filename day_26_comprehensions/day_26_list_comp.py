####### List Comprehension #######

# list comprehension can create new lists from an already created one
#to add a number to list
numbers = [1, 2, 3, 4]
#this is basically the way it should look(using keywords)
#new_list = [new_item for item in list]
new_list = [num + 1 for num in numbers]
#print(new_list)

#You dont only have to work with lists
name = "Dread"
new_list2 = [letter for letter in name]
#print(new_list2)

#list comprehension works on these sequances
#python Sequences:
#list
#range
#string
#tuple
#for n in range(1,5,2):

new_list3 = [n*2 for n in range(1, 5)]
#print(new_list3)

######## Conditional List Comprehension #########
#new_list = [new_item for item in list if test]
#the if test allows us to only perform the code if the test passes
names = ['Dread', 'ford', 'Ruthie', 'Jolie', 'Gabe']
Cap_names = [name.upper() for name in names if len(name) >= 5 ]
print(Cap_names)