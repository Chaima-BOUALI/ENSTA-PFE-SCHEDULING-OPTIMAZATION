"""Scheduling building blocks
Scheduling is the act of creating a schedule, which is a timetable for planned occurrences. Scheduling may also involve allocating resources to activities over time.

A scheduling problem can be viewed as a constraint satisfaction problem or as a constrained optimization problem. Regardless of how it is viewed, a scheduling problem is defined by:

-A set of time intervals, to define activities, operations, or tasks to be completed
-A set of temporal constraints, to define possible relationships between the start and end times of the intervals
-A set of specialized constraints, to specify of the complex relationships on a set of intervals due to the state and finite capacity of resources."""

"""Realized by Chaima BOUALI -Tutorial: Getting started with Scheduling in CPLEX for Python"""
#When using a cloud solving solution, the following attributes must be set with appropriate values:
url = None
key = None
#Creation of the model
import sys
from docplex.cp.model import *
import pandas as pd
import numpy as np

import sys
from docplex.cp.model import *
import docplex.cp.utils_visu as visu
import matplotlib.pyplot as plt
mdl0 = CpoModel()

#matplotlib inline
#Change the plot size
from pylab import rcParams
rcParams['figure.figsize'] = 15, 3
from datetime import datetime as dt

#data readers from csv
import csv


tData=time.time()
#Declarations of decision variables¶
masonry = mdl0.interval_var(size=35)
carpentry = mdl0.interval_var(size=15)
plumbing = mdl0.interval_var(size=40)
ceiling = mdl0.interval_var(size=15)
roofing = mdl0.interval_var(size=5)
painting = mdl0.interval_var(size=10)
windows = mdl0.interval_var(size=5)
facade = mdl0.interval_var(size=10)
garden = mdl0.interval_var(size=5)
moving = mdl0.interval_var(size=5)


#Adding the constraints
mdl0.add( mdl0.end_before_start(masonry, carpentry) )
mdl0.add( mdl0.end_before_start(masonry, plumbing) )
mdl0.add( mdl0.end_before_start(masonry, ceiling) )
mdl0.add( mdl0.end_before_start(carpentry, roofing) )
mdl0.add( mdl0.end_before_start(ceiling, painting) )
mdl0.add( mdl0.end_before_start(roofing, windows) )
mdl0.add( mdl0.end_before_start(roofing, facade) )
mdl0.add( mdl0.end_before_start(plumbing, facade) )
mdl0.add( mdl0.end_before_start(roofing, garden) )
mdl0.add( mdl0.end_before_start(plumbing, garden) )
mdl0.add( mdl0.end_before_start(windows, moving) )
mdl0.add( mdl0.end_before_start(facade, moving) )
mdl0.add( mdl0.end_before_start(garden, moving) )
mdl0.add( mdl0.end_before_start(painting, moving) )
# Solve the model
print("\nSolving model....")
#msol0 = mdl0.solve(url=url, key=key, TimeLimit=10)
print("done")