import sys,os

idim=# "number of MEP steps"
title='%s' % sys.argv[1].split('.')[0]
logpath=os.getcwd()
table=''

def energy(log):
    nstate=1
    input=open(log,'r').read().splitlines()
    for line in input:
        if 'Number of root(s) required' in line:
            nstate=int(line.split()[-1])
            break
    cas=[]
    pt2=[]
    en=[]
#    en=[0 for x in range(nstate*2)]
    for line in input:
        if '::    RASSCF root number' in line:
            state=int(line.split()[4])
            val=float(line.split()[-1])
            cas.append(val)
#            en[state-1]=val
        if '::    CASPT2 Root' in line:
            state=int(line.split()[3])
            val=float(line.split()[-1])
            pt2.append(val)
#            en[nstate+state-1]=val
    en=sorted(cas)+sorted(pt2)
    en=''.join(['%16.8f' % (x) for x in en])

    return en

for i in range(idim):
    crntname='%s-%d' % (title,i+1)
    crntpath='%s/%s' % (logpath,crntname)
    log='%s/%s.log' % (crntpath,crntname)
    table+='%-5d %s\n' % (i+1,energy(log))

out=open('energy.txt','w')
out.write(table)
out.close()
