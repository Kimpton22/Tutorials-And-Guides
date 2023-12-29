import os,sys

def batch(name,path,logpath,add):

    script="""#!/bin/sh
## script for OpenMalCas
## $INPUT and $WORKDIR do not belong to OpenMolCas
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=10:00:00
#SBATCH --job-name=%s
#SBATCH --partition=short
#SBATCH --mem=3Gb
#SBATCH --output=%%j.o.slurm
#SBATCH --error=%%j.e.slurm
#SBATCH --constraint="[broadwell|haswell|cascadelake]"

export INPUT=%s
export WORKDIR=%s

export MOLCAS_NPROCS=$SLURM_NTASKS
export MOLCAS_MEM=1870
export MOLCAS_PRINT=3
export MOLCAS_PROJECT=$INPUT
export MOLCAS_WORKDIR=$WORKDIR
export OMP_NUM_THREADS=1
export MOLCAS=/work/lopez/Molcas
export PATH=$MOLCAS/bin:$PATH

cd $WORKDIR
date                 >> %s/logfile.txt
$MOLCAS/bin/pymolcas -f $INPUT.inp -b 1
rm -r $MOLCAS_PROJECT
echo "$WORKDIR DONE" >> %s/logfile.txt
date                 >> %s/logfile.txt
echo ""              >> %s/logfile.txt

%s
""" % (name,name,path,logpath,logpath,logpath,logpath,add)

    return script

def Addscript(crntname,crntpath,nxtname,nxtpath,i,idim):
    script=''
    if i+1 < idim:
        script='''cp %s/%s.RasOrb %s/%s.StrOrb
cd %s
sbatch Srun_molcas.sh''' % (crntpath,crntname,nxtpath,nxtname,nxtpath)
    return script

idim=# "number of MEP steps"
title='%s' % sys.argv[1].split('.')[0]
inptemp=open(sys.argv[1],'r').read()
guessorb=open('%s.StrOrb' % (title),'r').read()
logpath=os.getcwd()
coordpath='%s/coord' % (logpath)
for i in range(idim):
    crntname='%s-%d' % (title,i+1)
    crntpath='%s/%s' % (logpath,crntname)
    nxtname='%s-%d' % (title,i+2)
    nxtpath='%s/%s' % (logpath,nxtname)
    if os.path.exists('%s' % (crntpath)) == False:
        os.makedirs('%s' % (crntpath))

    inp=open('%s/%s.inp' % (crntpath,crntname), 'w')
    inp.write(inptemp)
    inp.close()
    coord=open('%s/%s.xyz' % (coordpath,crntname),'r').read()
    xyz=open('%s/%s.xyz' % (crntpath,crntname), 'w')
    xyz.write(coord)
    xyz.close()
    orb=open('%s/%s.StrOrb' % (crntpath,crntname), 'w')
    orb.write(guessorb)
    orb.close()
    shll=open('%s/run_molcas.sh' % (crntpath),'w')
    shll.write(batch(crntname,crntpath,logpath,''))
    shll=open('%s/Srun_molcas.sh' % (crntpath),'w')
    shll.write(batch(crntname,crntpath,logpath,Addscript(crntname,crntpath,nxtname,nxtpath,i,idim)))
