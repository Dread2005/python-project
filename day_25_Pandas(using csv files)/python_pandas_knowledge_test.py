import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squ_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squ_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squ_count = len(data[data["Primary Fur Color"] == "Cinnamon"])


data_dic = {"fur color": ["cinnamon", "black", "grey"],
            "count": [cinnamon_squ_count, black_squ_count, gray_squ_count]}
my_data = pandas.DataFrame(data_dic)
print(my_data)
my_data.to_csv("squiral_count.csv")

