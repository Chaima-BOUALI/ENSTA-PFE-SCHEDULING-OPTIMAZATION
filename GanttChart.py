"""Drawing a Gantt Chart Using Python"""
#Chaima BOUALI copyright

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta
data = pd.read_csv("Scheduling.csv")
print(data)
#Convert data str to datetime data type, YYYY_MM_DD
data["START"] = pd.to_datetime(data["START"], format="%Y_%m_%d")
data["END"] = pd.to_datetime(data["END"], format="%Y_%m_%d")

#Sorting the tasks by STARTING DATE 
data.sort_values("START",axis=0,ascending=True, inplace=True)
#Reseting index inplace
data.reset_index(drop = True, inplace=True)

#Adding duration Column
data["DURATION"] = data["END"] - data ["START"] + timedelta(days = 1)

#Adding Columni : start date for each task wrt the project day 1
data["PastTime"] = data["START"] - data ["START"][0]

#print (data)

#Starting drawing 
nrow =len(data)
plt.figure(num=1, figsize=[8,5], dpi=100)
bar_width = 0.9

for i in range (nrow):
    i_rev = nrow - 1 - i 
    #Plot the last task
    plt.broken_barh([(data["START"][i_rev], data["DURATION"][i_rev])], (i - bar_width / 2, bar_width), color = "#8c172e")
    plt.broken_barh([(data["START"][0], data["PastTime"][i_rev])], (i - bar_width / 2, bar_width), color = "#f2f2f2")

y_pos = np.arange(nrow)
plt.yticks(y_pos, labels=reversed(data["TASK"]))
#xticks 
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(fmt="%b-%y"))
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0))
#Grid 
plt.grid(axis="x", which="major", lw=1)
plt.grid(axis="x", which="major", ls="--", lw=1)

plt.gcf().autofmt_xdate(rotation=30)
plt.xlim(data["START"][0])
plt.xlabel("DATE", fontsize=15, weight="bold")
plt.title("Testing Scheduling in python through SVC file", fontsize=25, weight="bold", color="#8e172c")
plt.tight_layout(pad=1.8)
plt.show()

