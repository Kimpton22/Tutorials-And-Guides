# CASPT2 - Vertical Excitation Energy
Second-order multiconfigurational perturbation theory is used in the program CASPT2 to compute the (dynamic) correlation energy.

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

