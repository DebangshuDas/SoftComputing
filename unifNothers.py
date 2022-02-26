import pandas as pd                           # pandas is a software library written for the Python programming language for data manipulation and analysis
import numpy as np
import random as rand
# import csv

def unif(seed,low,high):
    m = 2147483647
    a = 16807
    b = 127773
    c = 2836
    k=int(seed[0]/b)
    seed[0] = a*(seed[0]%b)-k*c
    if seed[0]<0:
        seed[0]=seed[0]+m
    val01=seed[0]/m
    return (low + int(val01*(high-low+1)))

def random_input(a,jobs,mcs,timeseed):
    mat = [ [0]*501 for _ in range(21) ]
    seed=[]
    seed.append(timeseed)
    for j in range(mcs):
        for i in range(jobs):
            mat[j][i] = unif(seed,1,99)
    for i in range(jobs):
        for j in range(mcs):
            a[i][j] = mat[j][i]

df = pd.read_excel("C:\\Users\\deban\\OneDrive\\Documents\\Workspace\\Soft-computing Project\\Taillard.xls", usecols=range(0,5), nrows=30, skiprows=2, header=None)  # parsing the excel file and storing in a pandas dataframe
data = df.to_numpy()
ind=rand.randint(0,29)
a=[ [0]*501 for _ in range(21) ]
jobs=20
mcs=5
timeseed=873654221
random_input(a,jobs,mcs,timeseed)
# for i in range(jobs,0,-1):
#     for j in range(mcs,0,-1):
#         a[i][j]=a[i-1][j-1]
b=[ [0]*mcs for _ in range(jobs)]
for i in range(0,jobs):
    for j in range(0,mcs):
        b[i][j] = a[i][j]
# print("\nJob matrix (Jobs="+str(jobs)+", Machines="+str(mcs)+"):\n")
# for i in range(0,jobs):
#     for j in range(0,mcs):
#         print(a[i][j],"\t",end="")
#     print()



# with open('D:\Documents\softComputing\output.csv', 'w', newline='') as csv_1:
#     csv_out = csv.writer(csv_1)
#     csv_out.writerows(a)

df1 = pd.DataFrame(b)
df1.to_csv('C:\\Users\\deban\\OneDrive\\Documents\\Workspace\\Soft-computing Project\\output.csv', index=2, header=2)