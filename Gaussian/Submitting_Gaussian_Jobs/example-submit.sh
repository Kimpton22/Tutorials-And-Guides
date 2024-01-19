#!/bin/bash
#SBATCH --job-name=syn-ladderdiene-wB97XD
#SBATCH --input=syn-ladderdiene-wB97XD.com
#SBATCH --partition=lopez
#SBATCH --time=3-00:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --mem=16G
#SBATCH --output=%j.o.slurm
#SBATCH --error=%j.e.slurm

hostname

export g16root=/work/lopez/
. $g16root/g16/bsd/g16.profile

work=`pwd`

export GAUSS_SCRDIR=$WORKING_DIR

cd $work
time $g16root/g16/g16 syn-ladderdiene-wB97XD.com
