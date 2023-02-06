#Chaima BOUALI Chapter 1. Introduction to Scheduling
#Imports and variables 
import sys
from docplex.cp.model import *
import docplex.cp.utils_visu as visu
import matplotlib.pyplot as plt
#Change the plot size
from pylab import rcParams
rcParams['figure.figsize'] = 15, 3
#Declarations of decision variables
url = None
key = None
mdl0=CpoModel()
masonry = (CpoModel()).interval_var(size=35)
carpentry = (CpoModel()).interval_var(size=15)
plumbing = (CpoModel()).interval_var(size=40)
ceiling = (CpoModel()).interval_var(size=15)
roofing = (CpoModel()).interval_var(size=5)
painting = (CpoModel()).interval_var(size=10)
windows = (CpoModel()).interval_var(size=5)
facade = (CpoModel()).interval_var(size=10)
garden = (CpoModel()).interval_var(size=5)
moving = (CpoModel()).interval_var(size=5)
#Adding the constraints
(CpoModel()).add( (CpoModel()).end_before_start(masonry, carpentry) )
(CpoModel()).add( (CpoModel()).end_before_start(masonry, plumbing) )
(CpoModel()).add( (CpoModel()).end_before_start(masonry, ceiling) )
(CpoModel()).add( (CpoModel()).end_before_start(carpentry, roofing) )
(CpoModel()).add( (CpoModel()).end_before_start(ceiling, painting) )
(CpoModel()).add( (CpoModel()).end_before_start(roofing, windows) )
(CpoModel()).add( (CpoModel()).end_before_start(roofing, facade) )
(CpoModel()).add( (CpoModel()).end_before_start(plumbing, facade) )
(CpoModel()).add( (CpoModel()).end_before_start(roofing, garden) )
(CpoModel()).add( (CpoModel()).end_before_start(plumbing, garden) )
(CpoModel()).add( (CpoModel()).end_before_start(windows, moving) )
(CpoModel()).add( (CpoModel()).end_before_start(facade, moving) )
(CpoModel()).add( (CpoModel()).end_before_start(garden, moving) )
(CpoModel()).add( (CpoModel()).end_before_start(painting, moving) )
# Calling the solve

msol0 = mdl0.solve()
msol0 = mdl0.solve(url=url, key=key, TimeLimit=10)
print("\nSolving model....")
#Displaying the solution
var_sol = msol0.get_var_solution(masonry)
print("Masonry : {}..{}".format(var_sol.get_start(), var_sol.get_end()))
var_sol = msol0.get_var_solution(carpentry)
print("Carpentry : {}..{}".format(var_sol.get_start(), var_sol.get_end()))
var_sol = msol0.get_var_solution(plumbing)
print("Plumbing : {}..{}".format(var_sol.get_start(), var_sol.get_end()))
var_sol = msol0.get_var_solution(ceiling)
print("Ceiling : {}..{}".format(var_sol.get_start(), var_sol.get_end()))
var_sol = msol0.get_var_solution(roofing)
print("Roofing : {}..{}".format(var_sol.get_start(), var_sol.get_end()))
var_sol = msol0.get_var_solution(painting)
print("Painting : {}..{}".format(var_sol.get_start(), var_sol.get_end()))
var_sol = msol0.get_var_solution(windows)
print("Windows : {}..{}".format(var_sol.get_start(), var_sol.get_end()))
var_sol = msol0.get_var_solution(facade)
print("Facade : {}..{}".format(var_sol.get_start(), var_sol.get_end()))
var_sol = msol0.get_var_solution(moving)
print("Moving : {}..{}".format(var_sol.get_start(), var_sol.get_end()))
#Graphic modeling of the solution
wt = msol0.get_var_solution(masonry)   
visu.interval(wt, 'lightblue', 'masonry')   
wt = msol0.get_var_solution(carpentry)   
visu.interval(wt, 'lightblue', 'carpentry')
wt = msol0.get_var_solution(plumbing)   
visu.interval(wt, 'lightblue', 'plumbing')
wt = msol0.get_var_solution(ceiling)   
visu.interval(wt, 'lightblue', 'ceiling')
wt = msol0.get_var_solution(roofing)   
visu.interval(wt, 'lightblue', 'roofing')
wt = msol0.get_var_solution(painting)   
visu.interval(wt, 'lightblue', 'painting')
wt = msol0.get_var_solution(windows)   
visu.interval(wt, 'lightblue', 'windows')
wt = msol0.get_var_solution(facade)   
visu.interval(wt, 'lightblue', 'facade')
wt = msol0.get_var_solution(moving)   
visu.interval(wt, 'lightblue', 'moving')
visu.show()
print("done")
