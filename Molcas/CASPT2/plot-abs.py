from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource
from matplotlib import cm
from matplotlib.ticker import StrMethodFormatter
import matplotlib.colors as col
import matplotlib.pyplot as plt
import numpy as np
import sys,json
import matplotlib as mpl
import math
##mpl.rc('font',family='Arial') ## might be commented out if now work

title='abs-dbh-unsub-wigner' # title of this figure

data=np.loadtxt('data.txt')

x=np.arange(len(data))
e0, e1, e2, e3, f1, f2, f3 = data.T
#convert the energy values from hartrees to units of wavelength in nm
e1=1239.84193/((e1-e0)*27.211)
e2=1239.84193/((e2-e0)*27.211)
e3=1239.84193/((e3-e0)*27.211)
et=np.concatenate([e1,e2])
et=np.concatenate([et,e3])
ft=np.concatenate([f1,f2])
ft=np.concatenate([ft,f3])
lim=[100,500,0.5]
fwhm=8

def abs(i,X,Y,fwhm):
    g=0
    c=fwhm/(2*(2*0.69314718055994529)**0.5)   #2ln2
    for t in range(len(X)):
        g+=Y[t]*math.e**(-1*(i-X[t])**2/(2*c**2))
    return g

x=np.arange(lim[0],lim[1]+0.1,lim[2])

y1=[]
y2=[]
y3=[]
yt=[]
for i in x:
    y1.append(abs(i,e1,f1,fwhm))
    y2.append(abs(i,e2,f2,fwhm))
    y3.append(abs(i,e3,f3,fwhm))
    yt.append(abs(i,et,ft,fwhm))
y1x=np.array(y1)
y2x=np.array(y2)
y3x=np.array(y3)
scale=np.max(y3x)
y1/=scale
y2/=scale
y3/=scale
print(max(y1))
print(max(y2))
print(max(y3))
#Normalize all of the absorbances so that the max value is just equal to 1
#Printing some of the max values to check them
#print(np.amax(e1),np.amin(e1))
#print(np.amax(f1),np.amin(f1))
#print(np.amax([y1,y2,y3]))
#print('S1', np.amax(y1))

#tot = len(idx)
#for c in [c2, c3, c4]:
#    v1 = 0
#    v2 = 0
#    v3 = 0
#    v4 = 0
#    v5 = 0
#    v6 = 0
#    for v in c:
#        if   v == 1:
#            v1 += 1
#        elif v == 2:
#            v2 += 1
#        elif v == 3:
#            v3 += 1
#        elif v == 4:
#            v4 += 1
#        elif v == 5:
#            v5 += 1
#        elif v == 6:
#            v6 += 1

 #   print('csf1(D) %6.2f csf2(D) %6.2f csf3(D) %6.2f csf4(ππ2) %6.2f csf5(ππ1) %6.2f csf6(0) %6.2f' % (v1/tot, v2/tot, v3/tot, v4/tot, v5/tot, v6/tot))

### Figure 1
fig=plt.figure()
ax = fig.add_subplot()
ax.spines['right'].set_visible(True)
ax.spines['top'].set_visible(True)
ax.axes.tick_params(axis='both',direction='in')
plt.subplots_adjust(wspace=0.3,hspace=0.3,bottom=0.15,left=0.15,right=0.85)
#### Format
xlabel=np.arange(100,451,100)
ylabel=np.arange(0,1.01,0.2)
ax.set_xlabel('Wavelength (nm)',fontsize=14,labelpad=3)
ax.set_ylabel(r'Intensity',fontsize=14,labelpad=3)
ax.axes.tick_params(axis='both',direction='in')
ax.set_xticks(xlabel)
ax.set_xticklabels(xlabel,fontsize=14)
ax.set_xlim(135,350)
ax.set_yticks(ylabel)
ax.set_yticklabels(ylabel,fontsize=14)
ax.set_ylim(0,1.1)

ax.set_aspect(1/ax.get_data_ratio()*1)
ax.xaxis.set_major_formatter(StrMethodFormatter('{x:.0f}'))
ax.yaxis.set_major_formatter(StrMethodFormatter('{x:.1f}'))

#### Plot data
#ax.plot(x,y4,color='green' ,marker='o',linewidth=3, markersize=0)
ax.plot(x,y3,color='green' ,marker='o',linewidth=1.5, markersize=0)
ax.plot(x,y2,color='blue'  ,marker='o',linewidth=1.5, markersize=0)
ax.plot(x,y1,color='red',marker='o',linewidth=1.5, markersize=0)
#ax.plot(x,yt,color='black' ,marker='o',linewidth=3, markersize=0,linestyle='--',alpha=0.5)

#plt.show()
fig.savefig('%s.png' % (title),bbox_inches='tight',dpi=400)

