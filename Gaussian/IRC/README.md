# 4. Intrinsic Reaction Coordinate (IRC) calculations
Intrinsic Reaction Coordinate (IRC) calculations start from the optimized TS geometry and attempt to explore the PES in both directions of descent (i.e. along the relevant reaction pathway). Note that for each TS there are exactly two directions of descent (which end in two distinct minima). By following these minimum pathways, IRCs can definitively show the two immediate minimum geometries that the TS of interest connects on the PES. These calculations are one of the most difficult to get to complete properly and are easier with larger imagniary (negative) frequency TSs. 
## References
IRC keyword info: [https://gaussian.com/irc/]

## Files necessary
```.com or .gjf (of an optimized TS) and .sh (not necessary if using python submit script)```

## Keywords and Usage
There is one mandatory keyword for IRCs which is ```IRC=(calcfc,recalc=1,maxpoints=X)```. The optional keywords ```calcfc and recalc=1``` are recommended here in every job to speed up the search and make it more likely for the IRC to complete successfully. Adding the option  ```maxpoints=X``` controls how many structures are calculated on the IRC surface. The default is 10, which is quite small, especially because maxpoints are split between each side of the TS (i.e. with maxpoints=10 5 points will be calculated on the left and 5 on the right of the TS). It is recommended to start this value at 30 to initially test if the calculations will be successful. If it is, this value can be increased until the PES is detailed enough.

### Optional Keywords
Within the "IRC" keyword, there are a number of optional modifiers that may aid your minimum geometry optimization. To use these, add them to the IRC keyword in this way: ```IRC=(OPTION1,OPTION2,OPTION3,...)```. Information for all options can be found here: [https://gaussian.com/irc/]
1. Forward and Reverse - These options ask the IRC to calculate in the "forward" or "reverse" directions only, or both if both options are added (while this is the default behavior of the IRC calculation, specifying both can be helpful for tricky IRCs). Note that forward and reverse are do not necessarily mean towards products or towards reactants; gaussian makes its own assignments for forward and reverse
2. stepsize=X - controls the maximum geometric change along the reaction pathway (similar to maxstep=X in optimization jobs). The default is 10 which corresponds to 0.1 bohr. Decrease this value and increase the maxpoints to increase the granularity of the PES.
3. LQA - This option can be useful when running into the error "Maximum number of corrector steps exceeded". Note that the addition of this keyword greatly increased the computational cost and will often require longer times, more processors, and should be given substantially more memory (try doubling it if possible).

## Analysis
1. Check the end of the ```.log``` file to confirm it has the line ```Normal Termination of Gaussian 16```, which confirms that the job finished successfully. If you do not have this line at the end of your file that means that the calculations failed (see common error messages to resolve this).
2. Open the ```.log``` file with GaussView. Right-click in the blue space to open the options and go down to "Results". Then click on "Vibrations...". This will bring up a box which shows the vibrational data of your molecule. You need to check that the first frequency is negative (<0) and that all other frequencies are positive (>0). This indicates that the electronic energy of the molecule increases all but one direction on the highly dimensional PES (i.e. that the structure is a TS).
3. You can create a video


