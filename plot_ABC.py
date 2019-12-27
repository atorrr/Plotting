# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:14:16 2019

@author: atorr
"""
import matplotlib.pyplot  as plt
import pandas as pd


"""
filen=str("weighted/1-3benzodioxole.gnuplot.weighted")
mol_name=str("1-3benzodioxole")
exp=[3.6288,	1.6284,	1.1364]
mini=-0.1*1000
h=0.26*1000
t=[7,130]
best=59
"""

"""
filen=str("weighted/1-hidroxynaphtalene.gnuplot.weighted")
mol_name=str("1-hidroxynaphtalene")
exp=[1.9239,	1.1058,	0.7025]
mini=-0.040*1000
h=0.150*1000
best=100
t=[7,100]
"""

"""
filen=str("weighted/2-hidroxynaphtalene.gnuplot.weighted")
mol_name=str("2-hidroxynaphtalene")
exp=[2.7691, 0.8218,	0.6340]
mini=-0.040*1000
h=0.150*1000
best=99
t=[7,100]
"""
"""
filen=str("weighted/7-azaindole.gnuplot.weighted")
mol_name=str("7-azaindole")
exp=[3.7444, 1.7017, 1.1705]
mini=-0.150*1000
h=0.550*1000
best=29
t=[6,350]
"""

#"""
filen=str("weighted/p-toluidine.gnuplot.weighted")
mol_name=str("p-toluidine")
exp=[5.3131,	1.4795,	1.1581]
mini=-0.250*1000
h=0.400*1000
best=28
t=[6,100]
#"""

"""
filen=str("weighted/o-toluidine.gnuplot.weighted")
mol_name=str("o-toluidine")
exp=[3.1566,	2.1872,	1.2960]
mini=-0.100*1000
h=0.200*1000
best=86
t=[6,80]
#"""

#unfinished

"""
filen=str("weighted/2-5diphenyl1_3_4oxidiazole.gnuplot.weighted")
mol_name=str("2-5diphenyl1-3-4oxidiazole")
exp=[1.6299,	0.2135,	0.1885]
mini=-0.0500*1000
h=0.100*1000
best=24
t=[6,40]
#"""

"""
filen=str("weighted/2-5-diphenylfuran.gnuplot.weighted")
mol_name=str("2-5diphenylfuran")
exp=[1.4565,	0.2188,	0.1900]
mini=-0.0750*1000
h=0.10*1000
best=98
t=[6,17]
#"""


"""
filen=str("weighted/fluorene.gnuplot.weighted")
mol_name=str("fluorene")
exp=[2.1023,	0.5933,	0.4643]
mini=-0.050*1000
h=0.0850*1000
best=86
t=[6,23]
#"""


#"""
filen=str("weighted/3-toluidine.gnuplot.weighted")
mol_name=str("3-toluidine")
exp=[3.5366,	1.7888,	1.1974]
mini=-0.060*1000
h=0.230*1000
best=61
t=[6,123]
#"""

d=0

filen_gd3=str(filen)+".gd3"
print(filen_gd3)




#filen=str("file:///C:/Users/atorr/Desktop/sonora2019/x_resultados/rmsd/1-3benzodioxole.gnuplot.weighted.nogd3")
df=pd.read_csv(filen,  sep='\s+', index_col=0, header=None)
df.columns=['c1','c2','c3','c4','c5', 'c6', 'c7', 'c8']
c=[1,7,14,21,28,35,42,49,56,63,70,77,84,91,98,105]




col=['r','b','burlywood','chartreuse','r','b','burlywood','chartreuse','r','b','burlywood','chartreuse','r','b','burlywood','chartreuse']

xcf=["PBE1PBE", "PBEPBE", "B97D3", "B3LYP", "BLYP", "BP86", "BPBE", "B3PW91", "BMK", "M05", "MO52X", "M06L", "M06", "M062X", "M06HF" ]

fig = plt.figure() # Figure
ax = fig.add_subplot(111) # Axes
ax.set_xticklabels(c)
#ax1 = ax.twiny()
#ax1.set_xticklabels(xcf, rotation=90 )
plt.style.use('seaborn-white')

farbe=['red','crimson','tomato','darkorange','gold','greenyellow','lime','limegreen','mediumspringgreen', 'turquoise','aquamarine','cornflowerblue','mediumslateblue','violet','mediumorchid']


alph1=0.3
ax.bar(df.index[0], y=mini, width=6, align='edge', height=h, alpha=alph1, color=farbe[0])
ax.bar(df.index[6], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[1])
ax.bar(df.index[13], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[2])
ax.bar(df.index[20], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[3])
ax.bar(df.index[27], y=mini, width=7, align='edge', height=h, alpha=0.25, color=farbe[4])
ax.bar(df.index[34], y=mini, width=7, align='edge', height=h, alpha=0.40, color=farbe[5])
ax.bar(df.index[41], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[6])
ax.bar(df.index[48], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[7])
ax.bar(df.index[55], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[8])
ax.bar(df.index[62], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[9])
ax.bar(df.index[69], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[10])
ax.bar(df.index[76], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[11])
ax.bar(df.index[83], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[12])
ax.bar(df.index[90], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[13])
ax.bar(df.index[97], y=mini, width=7, align='edge', height=h, alpha=alph1, color=farbe[14])


#ax.xaxis.set_ticks_position('top')
#ax.set_xticklabels(xcf, rotation=90)

#ax1.xaxis.set_ticks_position('bottom')
#ax1.set_xticklabels(c)

if d==0:
    #not empirical dispersion
    plt.plot(df.index, (df.c2-exp[0])*1000, color='r', marker='d', label="A'", linewidth=0.60, fillstyle='none', markersize=4)
    plt.plot(df.index, (df.c3-exp[1])*1000, color='b', marker='o', label="B'", linewidth=0.60, fillstyle='none', markersize=4)
    plt.plot(df.index, (df.c4-exp[2])*1000, color='m', marker='s', label="C'", linewidth=0.60, fillstyle='none', markersize=4)

if d==1:
    #dispersion
    dfgd3=pd.read_csv(filen_gd3,  sep='\s+', index_col=0, header=None)
    dfgd3.columns=['c1','c2','c3','c4','c5', 'c6', 'c7', 'c8']
    plt.plot(dfgd3.index, (dfgd3.c2-exp[0])*1000, color='r', marker='x', label="A", linewidth=0.60, fillstyle='none', markersize=4)
    plt.plot(dfgd3.index, (dfgd3.c3-exp[1])*1000, color='b', marker='x', label="B", linewidth=0.60, fillstyle='none', markersize=4)
    plt.plot(dfgd3.index, (dfgd3.c4-exp[2])*1000, color='m', marker='x', label="C", linewidth=0.60, fillstyle='none', markersize=4)

plt.ylabel("$\Delta$ MHz", fontsize=16)
plt.xlabel("DFT methods", fontsize=16, fontweight='medium')
plt.xticks(c)
#plt2=plt.twiny()
#plt2.set_xticklabels(xcf)

plt.axhline(0.0, color='k', linewidth=0.50)
plt.axvline(best, color='k', linewidth=0.80, linestyle='--' )

plt.axis([1,105,mini,mini+h],14) 

plt.legend(loc=9)
plt.text(t[0], t[1], mol_name, fontsize=20, fontweight='bold')


