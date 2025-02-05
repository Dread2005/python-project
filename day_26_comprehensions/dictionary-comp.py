#new_dic = {new_key:new_value for item in list}
#or new_dic = {new_key:new_value for(key,value) in dict.items()}
#or new_dic = {new_key:new_value for(key,value) in dict.items() if (test)}
import random

###### dic_comp #######
names = ['Dread', 'ford', 'Ruthie', 'Jolie', 'Gabe']
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

####### looping through dict #######
passed_students = {student: score for (student, score) in student_scores.items() if score > 60}
print(passed_students)

#### list_comp ###
data_list = [key for (key, value) in student_scores.items()]
print(data_list)# will give you keys
