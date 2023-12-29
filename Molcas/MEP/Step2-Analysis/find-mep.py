## read Gaussian log file to extract interploted structures

import os,sys

input=open(sys.argv[1]).read().splitlines()
title=sys.argv[1].split('.')[0]

if len(sys.argv) <= 2:
    index=1
else:
    index=int(sys.argv[2])

read=0
natom=0
coord=[]

for n,line in enumerate(input):
    if '[N_GEO]' in line:
        geom=int(input[n+1])
        break
for n,line in enumerate(input):
    if '[GEOMETRIES]' in line:
        read=1
        natom=int(input[n+1])
        for i in range(geom):
            xyz=input[n+1+(natom+2)*i:n+1+(natom+2)*(i+1)]
            xyz='\n'.join([x for x in xyz])
            with open('%s-%s.xyz' % (title,index+i),'w') as out:
                out.write(xyz+'\n')
        break
