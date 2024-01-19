# Performing gaussian jobs with solvation
Implicit solvation is easily added to any gaussian job with the scrf keyword (you can read about this here: ```https://gaussian.com/scrf/```). This keyword places the solute inside of a cavity, whose surface becomes charged depending on the electronic topology of the solute molecule, providing some stabilization. The extent of this surface charge distribution depends on the dielectric constant of the chosen solvent. Most common solvents are available with gaussian, but if you have concerns double check the gaussian manual.
There are a few solvation methods which can be used. We usually use the "pcm" model which is good for initial calculations. For more refined free energies of solvation, it is recommended to use the "smd" method.
## Keyword and Usage
In addition to any other job keywords, add this keyword to have implicit solvation:

scrf=(SOLVATION_METHOD, solvent=SOLVENT)
