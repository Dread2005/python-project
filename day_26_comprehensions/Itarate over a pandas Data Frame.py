import pandas

student_dict = {"student": ['Dread', 'ford', 'Ruthie', 'Jolie', 'Gabe'],
                "score": [78, 73,  59,  51, 18]}

#####looping through dict using "for" loop######
#for (key, value) in student_dict.items():
    #print(value)

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

######## looping through Data Frame Rows ########
for (index, row) in student_data_frame.iterrows():
    #print(index)
    #print(row)
    #print(row.student)
    #print(row.score)
    if row.student == "Dread":
        print(row.score)
