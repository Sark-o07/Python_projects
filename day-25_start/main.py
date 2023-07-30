# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd
#
data = pd.read_csv("weather_data.csv")
print(data)
# print(data["Primary Fur Color"])
# data_to_dict = data.to_dict()
# print(data_to_dict)
# temp_list = data["temp"].to_list()
# temp_sum = 0
# for temp in temp_list:
#     temp_sum += temp
#     print(temp_sum)
#
# mean = temp_sum/len(temp_list)
# print(mean)
# print(data.temp.mean())


def converter(c):
    return (c * 9/5) + 32


monday = data[data.day == "Monday"]
print(monday)
monday_temp = monday.temp
print(converter(monday_temp))
# colors = ["Gray", "Black", "Cinnamon"]
#
#
# def count(color):
#     squirrel_color_count = data[data["Primary Fur Color"] == color]
#     return squirrel_color_count["Primary Fur Color"].count()

#
# Count = []
# for i in colors:
#     num = count(i)
#     Count.append(num)
#
# count_dict = {"Color": colors, "Count": Count}
# count_df = pd.DataFrame(count_dict)
# count_df.to_csv("squirrel_count.csv")









