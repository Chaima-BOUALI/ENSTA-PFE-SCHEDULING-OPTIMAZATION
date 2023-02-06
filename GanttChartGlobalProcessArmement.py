"""Drawing a Gantt Chart Using Python"""
#Chaima BOUALI copyright

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta
data = pd.read_csv("GlobalProcessSimulationBPMNResults.csv")
print(data)
#Convert data str to float data type
data["min"] = data["min"].astype (float)
data["max"] = data["max"].astype (float)

#Sorting the tasks by STARTING DATE 
data.sort_values("min",axis=0,ascending=True, inplace=True)
#Reseting index inplace
data.reset_index(drop = True, inplace=True)

#Adding duration Column
data["AVG"] = data["max"] - data ["min"] 

#Adding Column : start date for each task wrt the project day 1
data["PastTime"] = data["min"] - data ["min"][0]

print (data)

#Starting drawing 
nrow =len(data)
plt.figure(num=1, figsize=[8,5], dpi=100)
bar_width = 0.9

for i in range (nrow):
    i_rev = nrow - 1 - i 
    #Plot the last task
    plt.broken_barh([(data["min"][i_rev], data["AVG"][i_rev])], (i - bar_width / 2, bar_width), color = "#0080FF")
    plt.broken_barh([(data["min"][0], data["PastTime"][i_rev])], (i - bar_width / 2, bar_width), color = "#A5CBE2")

y_pos = np.arange(nrow)
plt.yticks(y_pos, labels=reversed(data["Scenario id."]))
"""#xticks 
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(fmt="%b-%y"))
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0))"""
#Grid 
plt.grid(axis="x", which="major", lw=1)
plt.grid(axis="y", which="major", ls="--", lw=1)

plt.gcf().autofmt_xdate(rotation=30)
plt.xlim(data["min"][0])
plt.xlabel("TIME", fontsize=10, weight="bold")
plt.title("Autogenerated GanttDiagram in python through SVC Pragmadev file", fontsize=10, weight="bold", color="#0F056B")
plt.tight_layout(pad=2.5)
plt.show()