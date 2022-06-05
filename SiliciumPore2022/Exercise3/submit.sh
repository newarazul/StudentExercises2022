#!/bin/bash
##SBATCH -n 40
#SBATCH --nodes=1
#SBATCH --tasks-per-node=40
#SBATCH --time=00:10:00
#SBATCH --partition=short
#SBATCH -A hpc-prf-instpra
 
module use /cm/shared/apps/pc2/CHEM_PHYS_SW/modules
module load chem/CP2K/8.1_gnu

srun --cpu_bind=rank cp2k.psmp -i [].inp -o [].out
