#!/bin/sh
## script for OpenMalCas
## $INPUT and $WORKDIR do not belong to OpenMolCas
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=20-00:00:00
#SBATCH --job-name=meci-homoE
#SBATCH --partition=lopez
#SBATCH --mem=10Gb
#SBATCH --output=%j.o.slurm
#SBATCH --error=%j.e.slurm

export INPUT=meci-homoE
export WORKDIR=$PWD

export MOLCAS_NPROCS=1
export MOLCAS_MEM=1870
export MOLCAS_PRINT=3
export MOLCAS_PROJECT=$INPUT
export MOLCAS_WORKDIR=$WORKDIR
export OMP_NUM_THREADS=$SLURM_NTASKS
export MOLCAS=/work/lopez/Molcas

module load python/3.7.1

cd $WORKDIR
$MOLCAS/bin/pymolcas -f $INPUT.inp -b 1
rm -r $MOLCAS_PROJECT
