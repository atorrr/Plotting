# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:14:16 2019

@author: atorr
"""
import matplotlib.pyplot  as plt
import pandas as pd



#"""
filen=str("weighted/1-3benzodioxole.gnuplot.weighted")
mol_name=str("1-3benzodioxole")
filen_gd3=str(filen)+".gd3"
ymin= [0.005500237 , 59] #no disp
ymingd3= [0.0037 , 59] #disp
h=0.07
d=0
t=[7,0.06] #text pos
#"""

"""
filen=str("weighted/1-hidroxynaphtalene.gnuplot.weighted")
mol_name=str("1-hidroxynaphtalene")
filen_gd3=str(filen)+".gd3"
ymingd3= [0.004834293, 100] #disp
ymin= [0.004817865, 100] #no disp
d=0
h=0.07
t=[7,0.06] #text pos
"""

"""
filen=str("weighted/2-hidroxynaphtalene.gnuplot.weighted")
mol_name=str("2-hidroxynaphtalene")
filen_gd3=str(filen)+".gd3"
ymin= [0.001996504,  99] #no disp
ymingd3= [0.001877576,  99] #disp
d=0
h=0.07
t=[7,0.06] #text pos
"""

"""
filen=str("weighted/7-azaindole.gnuplot.weighted")
mol_name=str("7-azaindole")
filen_gd3=str(filen)+".gd3"
ymin= [0.035179857,      29] #no disp
ymingd3= [0.034164527,     29] #disp
d=0
h=0.2
t=[7,0.1706] #text pos
"""

#"""
filen=str("weighted/p-toluidine.gnuplot.weighted")
mol_name=str("p-toluidine")
filen_gd3=str(filen)+".gd3"
ymin= [0.006156102,   28] #no disp
ymingd3= [0.006572192,     28] #disp
d=0
h=0.127
t=[7,0.106] #text pos
#"""

"""
filen=str("weighted/o-toluidine.gnuplot.weighted")
mol_name=str("o-toluidine")
filen_gd3=str(filen)+".gd3"
ymin= [0.003016693,   86] #no disp
ymingd3= [0.003004549,     86] #disp
d=0
h=0.05
t=[7,0.046] #text pos
#"""

#unfinished

#"""
filen=str("weighted/2-5diphenyl1_3_4oxidiazole.gnuplot.weighted")
mol_name=str("2-5diphenyl1-3-4oxidiazole")
filen_gd3=str(filen)+".gd3"
ymin= [0.000525667,      24] #no disp
ymingd3= [0.000170291,      52] #disp
d=0
h=0.023
t=[2,0.0213] #text pos
"""

"""
filen=str("weighted/2-5-diphenylfuran.gnuplot.weighted")
mol_name=str("2-5diphenylfuran")
filen_gd3=str(filen)+".gd3"
ymin=  [0.000458031,      98]#no disp
ymingd3= [0.001139857,      70] #disp
d=0
h=0.033
t=[2,0.0283] #text pos
#"""


"""
filen=str("weighted/fluorene.gnuplot.weighted")
mol_name=str("fluorene")
filen_gd3=str(filen)+".gd3"
ymin=  [0.000382718,      86]#no disp
ymingd3= [0.000123659,      26] #disp
d=0
h=0.028
t=[4,0.025] #text pos
#"""

#"""
filen=str("weighted/3-toluidine.gnuplot.weighted")
mol_name=str("3-toluidine")
filen_gd3=str(filen)+".gd3"
ymin=  [0.000210695 ,     61]#no disp
ymingd3= [0.001368994,     60] #disp
d=0
h=0.064
t=[4,0.05] #text pos
#"""



if ymin[0]<ymingd3[0]:
    d=0
    ming=ymin[0]
if ymin[0]>ymingd3[0]:
    d=1
    ming=ymingd3[0]

d=1  #plot or not gd3
    
print(d)

if d==1:
    ymin=ymingd3

#filen=str("file:///C:/Users/atorr/Desktop/sonora2019/x_resultados/rmsd/1-3benzodioxole.gnuplot.weighted.nogd3")


df=pd.read_csv(filen,  sep='\s+', index_col=0, header=None)
df.columns=['c1','c2','c3','c4','c5', 'c6', 'c7', 'c8']
c=[1,7,14,21,28,35,42,49,56,63,70,77,84,91,98,105]
dfgd3=pd.read_csv(filen_gd3,  sep='\s+', index_col=0, header=None)
dfgd3.columns=['c1','c2','c3','c4','c5', 'c6', 'c7', 'c8']

xcf=["PBE1PBE", "PBEPBE", "B97D3", "B3LYP", "BLYP", "BP86", "BPBE", "B3PW91", "BMK", "M05", "MO52X", "M06L", "M06", "M062X", "M06HF" ]
fig = plt.figure(u'Gráfica de barras') # Figure
ax = fig.add_subplot(111) # Axes
plt.style.use('seaborn-white')
mini=0


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

#ax.bar(df.index[0], width=6, align='edge', height=0.07, alpha=alph1, color='firebrick')
#ax.bar(df.index[6], width=7, align='edge', height=0.07, alpha=alph1, color='crimson')


plt.plot(df.index, df.c1, color='k', marker='o', label="no gd3", linewidth=0.60, fillstyle='none', markersize=4)

if d==1:
    plt.plot(dfgd3.index, dfgd3.c1, color='g', marker='x', label="gd3", linewidth=0.60, markersize=4)


#plt.title(mol_name, fontsize=20, fontweight='bold')
plt.ylabel("RMSD", fontsize=16)
plt.xlabel("DFT methods", fontsize=16, fontweight='medium')
plt.xticks(c)
plt.axhline(ming, color='g', linewidth=0.50)

plt.axis([1,105,mini,mini+h],14) 

plt.legend(loc=0)
plt.text(t[0], t[1], mol_name, fontsize=20, fontweight='bold')
