# CASPT2 - Vertical Excitation Energy
Second-order multiconfigurational perturbation theory is used in the program CASPT2 to compute the (dynamic) correlation energy. XMS is the extended multistate method and the perturbations are computed with one common zeroth-order Hamiltonian.

## References
CASPT2: [https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/rasscf.html](https://molcas.gitlab.io/OpenMolcas/sphinx/users.guide/programs/caspt2.html)


## Files necessary
```.inp```,```.xyz```,```.sh``` and ```.StrOrb``` (RasOrb from Opt)

## Submission
You should have a directory with all the files mentioned before and use the following command to submit the job:
_Replace XXX.sh by your filename_

```
sbatch XXX.sh
```


## Analysis
1. Check .log and .status should have ```Happy landing!```
   
2. Check if the orbitals in the active space are still the same as optimization

3. Go to the end of the ```.log``` file by pressing ```SHIFT G```, next you will need to search for a specific keyword to find the data.
   
4. Search for State Energies using:
```
?XMS-CASPT2
```
_Remember to convert the energies to eV (multiply by 27.2114) and subtract the S0 Energy to get the VEE_
<img width="482" alt="Screenshot 2024-01-24 at 4 25 26 PM" src="https://github.com/Kimpton22/Tutorials-And-Guides/assets/100699955/4ef7f35c-f38c-4266-93bf-44ca6eb8c8ba">

_State 1 is the ground state_

5. Search for oscillator strength:
```
?Dipole transition strengths (spin-free states)
```
<img width="845" alt="Screenshot 2024-01-24 at 4 24 48 PM" src="https://github.com/Kimpton22/Tutorials-And-Guides/assets/100699955/334899da-8121-497f-9255-b4e070b33164">


# Absorption Spectrum
The XMS-CASPT2 will be computed for 500 non-equilibrium geometries using Wigner sampling and the results will be used to plot a spectrum


## Files necessary
```.inp```,```.xyz```, ```.StrOrb```,```.freq.molden```, ```control```,Gen-FSSH.py```, ```collector.sh```,``` plot-abs.py```
_Input, XYZ, and StrOrb are the same as XMS-CASPT2_
_.freq.molden from Opt_

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
_Number of molecules = nodes x cores_

5. To run submit the jobs, add in the first line of the runall.sh:  
```
 #!/bin/sh
```
6. Submit runall
```
sbatch runall.sh
```

## Analysis
1. Update ```collector.sh``` based on the number of excited states you want to extract energies and then extract the data using:
   ```
   sbatch collector.sh
   ```
3. Check generated ```data.txt```, and replace empty space (oscillator less than threshold) to 0. 
4. Plot spectrum - It will have S1 to S3
   ```
   python3 plot-abs.py
    ```
   ![abs-dbh-unsub-wigner](https://github.com/Kimpton22/Tutorials-And-Guides/assets/100699955/7e43ce50-611b-4605-b50e-2b7b256924d5)

