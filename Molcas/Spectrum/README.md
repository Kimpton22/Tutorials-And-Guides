# 6. Absorption Spectrum
## Files necessary
```.inp```,```.xyz```,```.sh```, ```.StrOrb```, ```control```, ```Gen-FSSH.py```. Input is the same as XMS-CASPT2

Scripts
```
/work/lopez/share_from_Leticia/model-scripts/spectrum
```

## Submission

1. Request resources
```
srun -N 1 --exclusive --partition=short --time=23:59:59 --pty /bin/bash
```
2. Load python
```
module load python/3.7.1
```

4. Generate input file and wigner samples - It will generate the wigner.xyz
```
python Gen-FSSH.py -x control
```
5. To run dynamics, add in the first line of the runall.sh:  
```
 #!/bin/sh
```
6. Submit runall

## Analysis
1. Use ```collector.sh``` to extract energies
   ```
   sbatch collector.sh
   ```
2. Check generated ```data.txt```, and replace blank oscillator to 0
3. Plot spectrum
   ```
   python3 plot-abs.py
   ````

