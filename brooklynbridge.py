#Samantha Michelle Garcia

import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

file ='Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project.csv'

df = pd.read_csv(file)

#print(df.head(5))

# value_counts() -- to see unique values

#print(df["lat"].value_counts()) #latitudinal position
#print(df["long"].value_counts()) #longitudinal position
#print(df["Location1"].value_counts()) #coordinates
#print(df["location"].value_counts()) #Brooklyn Bridge

#remove these columns since they all have just the same value

df = df.drop("lat", axis=1)
df = df.drop("long", axis=1)
df = df.drop("Location1", axis=1)
df = df.drop("location", axis=1)

#going to split the "hour_beginning" column into date and hour

df[["date", "time"]] = df.hour_beginning.str.split(" ", n=1, expand=True)
df = df.drop("hour_beginning", axis=1)

#print(df.dtypes)

df["date"] = pd.to_datetime(df["date"])

maximum = df["Pedestrians"].max()
minimum = df["Pedestrians"].min()
mean = df["Pedestrians"].mean()

months = df.groupby(df["date"].dt.month).size()
#print(months)

x = months.index
height = months.values
colors = ["red", "pink", "orange", "yellow", "green", "cyan", "teal", "blue", "indigo", "violet"]

plt.title("Brooklyn Bridge Pedestrian Counts per Month")
plt.bar(x, height, color=colors, tick_label=x)
plt.show()
