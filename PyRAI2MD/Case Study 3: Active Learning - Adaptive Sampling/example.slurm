#!/bin/sh
## script for OpenMalCas
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=23:59:59
#SBATCH --job-name=record100
#SBATCH --partition=short,lopez,long
#SBATCH --mem=20gb
#SBATCH --output=%j.o.slurm
#SBATCH --error=%j.e.slurm
#SBATCH --constraint="[broadwell|haswell|cascadelake|ib]"

if [ -d "/srv/tmp" ]
then
 export LOCAL_TMP=/srv/tmp
else
 export LOCAL_TMP=/tmp
fi
