"""Drawing a Gantt Chart Using Python"""
#Chaima BOUALI copyright

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta
data = pd.read_csv("internship_plannification.csv")
print(data)
#Convert data str to datetime data type, YYYY_MM_DD
data["DD_TOT"] = pd.to_datetime(data["DD_TOT"], format="%Y_%m_%d")
data["DD_TARD"] = pd.to_datetime(data["DD_TARD"], format="%Y_%m_%d")
data["DF_TOT"] = pd.to_datetime(data["DF_TOT"], format="%Y_%m_%d")
data["DF_TARD"] = pd.to_datetime(data["DF_TARD"], format="%Y_%m_%d")


#Sorting the tasks by best STARTING DATE 
data.sort_values("DD_TOT",axis=0,ascending=True, inplace=True)
#Reseting index inplace
data.reset_index(drop = True, inplace=True)

#Sorting the tasks by worst STARTING DATE 
data.sort_values("DD_TARD",axis=0,ascending=True, inplace=True)
#Reseting index inplace
data.reset_index(drop = True, inplace=True)

#Adding best duration Column
data["Best_DURATION"] = data["DF_TOT"] - data ["DD_TOT"] + timedelta(days = 1)
#Adding worst duration Column
data["Worst_DURATION"] = data["DF_TARD"] - data ["DD_TARD"] + timedelta(days = 1)
#Adding Columni : start date for each task wrt the project day 1
data["BestPastTime"] = data["DD_TOT"] - data ["DD_TOT"][0]
#Adding Columni : start date for each task wrt the project day 1
data["WorstPastTime"] = data["DD_TARD"] - data ["DD_TARD"][0]
print (data)

#Starting drawing 
nrow =len(data)
plt.figure(num=1, figsize=[8,5], dpi=100)
bar_width = 0.9

for i in range (nrow):
    i_rev = nrow - 1 - i 
    #Plot the last task
    plt.broken_barh([(data["DD_TOT"][i_rev], data["Best_DURATION"][i_rev])], (i - bar_width / 2, bar_width), color = "#8c172e")
    plt.broken_barh([(data["DD_TOT"][0], data["BestPastTime"][i_rev])], (i - bar_width / 2, bar_width), color = "#f2f2f2")
    #Plot the last task
    plt.broken_barh([(data["DF_TARD"][i_rev], data["Worst_DURATION"][i_rev])], (i - bar_width / 2, bar_width), color = "#0080ff")
    plt.broken_barh([(data["DF_TARD"][0], data["WorstPastTime"][i_rev])], (i - bar_width / 2, bar_width), color = "#a5cbe2")
y_pos = np.arange(nrow)
plt.yticks(y_pos, labels=reversed(data["Tâches_techniques"]), fontsize=5, color="#000000",style='oblique')
#xticks 
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(fmt="%b-%y"))
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0))
#Grid 
plt.grid(axis="x", which="major", lw=1)
plt.grid(axis="x", which="major", ls="--", lw=1)

plt.gcf().autofmt_xdate(rotation=30)
plt.xlim(data["DD_TOT"][0])
plt.xlim(data["DD_TARD"][0])

plt.xlabel("DATES", fontsize=5, weight="bold")
plt.title("Internship Plannification in python through SVC file", fontsize=10, weight="bold", color="#8e172c",style='oblique')
plt.tight_layout(pad=1.8)
plt.show()

