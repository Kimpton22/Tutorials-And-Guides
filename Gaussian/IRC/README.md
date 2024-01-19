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
     1. It is not uncommon for IRCs to fail. In a lot of cases this is ok, but un-ideal. It really depends on the number of succesful points the procedure was able to generate. To determine this, proceed to step 2. If there are too few points, you can play around with the various optional keywords to see if something works. However, some IRCs may not be possible to get, especially for small magnitude imaginary frequencies.
2. Open the ```.log``` file with GaussView. Right-click in the blue space to open the options and go down to "Results". Then click on "IRC/Path...". This will bring up a graph which the reaction pathway and energy along it. Points can be clicked on to show the geometry at each point. On either side of the IRC lie the reactant and product minima for this TS (their order depends on how gaussian defined the forward/reverse direction). It is important to check these minima to ensure that they are what you expect for the reaction. If they are not, then this means you've found a different TS which connects these two minima. The TS lies at the point highest in energy on this graph.
3. You can create a video of the reaction path. First find the reactant (as you have defined it) on the IRC surface. Then, in the top left there is a green circle with a drop down menu to its right. In this menu you can control the direction of the video and its speed (framerate). Once you have selected options, right-click in the blue space, go to "File" then "Save Movie", which allows you to save a video of the transformation. 


