#!/bin/sh
## script for OpenMalCas
## $INPUT and $WORKDIR do not belong to OpenMolCas
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=5-23:00:00
#SBATCH --job-name=bf3-tropone-augccpvdz-8-6-1-s0-opt-sa4
#SBATCH --partition=lopez
#SBATCH -w d3004
#SBATCH --mem=4Gb
#SBATCH --output=%j.o.slurm
#SBATCH --error=%j.e.slurm

export INPUT=bf3-tropone
export WORKDIR=$PWD

export MOLCAS_NPROCS=$SLURM_NTASKS
export MOLCAS_MEM=2870
export MOLCAS_PRINT=3
export MOLCAS_PROJECT=$INPUT
export MOLCAS_WORKDIR=$WORKDIR
export OMP_NUM_THREADS=1
export MOLCAS=/work/lopez/Molcas

module load python/3.7.1

cd $WORKDIR
$MOLCAS/bin/pymolcas -f $INPUT.inp -b 1
rm -r $MOLCAS_PROJECT

