import pandas
data = pandas.read_csv("weather_data.csv")
#(Dataframe) print(type(data))
#(Series)print(type(data["temp"]))

#there are 2 primary types of data structures, the Series(one dimensional), and Datafame(two dimensional)
######## Dataframe #########
#a dataframe is basically the pandas version of the whole shet of a excel.file

######## Series ###########
# a series is basically a column of a excel.file

#### The API reference is a list of all you can do
#data_dict = data.to_dict()
#print(data_dict)

####cALC AVER######
temp_list = data["temp"].to_list()
#range_ = len(temp_list)
#anverage = sum(temp_list) / range_
#print(average)
#temp_list.mean()

#####CALC MAX#######
max_ = data["temp"]
#data["temp"].max()
#print(max_.max())


#####Get data in Columns
#print(data["condition"])
#or use
#print(data.condition)

######get data in rows
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#print(monday.condition)

monday = data[data.day == "Monday"]
deg_c = monday.temp
deg_f = (deg_c * (9/5)) + 32
#print(deg_f)

#create Dataframe
data_dic = {
    "students": ["Amy", "Jane", "Dan"],
    "scores": [6, 73, 12]
}

my_data = pandas.DataFrame(data_dic)
print(my_data)

#Turn the Dataframe to CSV
my_data.to_csv("new_data.csv")



