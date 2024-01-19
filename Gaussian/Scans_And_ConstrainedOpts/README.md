# 1. Scans and Constrained Optimizations
Ground state geometry optimizations in gaussian look to minimize the energy of a structure by varying geometric parameters in the molecule. It does this using first and sometimes second order derivatives. Geometry optimizations will continue until a) a stationary point is reached on the potential energy surface (PES) (stationary points includes TSs and minima) b) an error causes the job to end early or c) the maximum number of geometry iterations is reached.
## References
Opt keyword info: [https://gaussian.com/opt/] (see options and modredundant for more information on constrained optimizations specifically)


## Files necessary
```.com or .gjf and .sh (not necessary if using python submit script)```

## Keywords and Usage
There is one mandatory keyword for geometry optimizations which is ```opt=modredundant```. ```opt``` asks gaussian to do a geometry optimization (searching for a minimum energy structure by default) and the ```modredundant``` option signals to gaussian that there are geometric constraints. 

Constraints and scans are added to the bottom of the ```.com/gjf``` file, after all xyz coordinated. Make sure that there is exactly one blank line separating the xyz coordinates and the constraints. There is no limit on the number of constraints you can add, however adding too many constraints often leads to errors in gaussian, so limit them as much as possible. 

Any geometric parameter can be constrained or scanned. This include bond lengths, angles and dihedrals. Constraints are set first by indicating the type (i.e. bond [B; requires 2 atoms], angle [A; requires 3 atoms], or dihedral [D; requires 4 atoms]) followed by the atom numbers you want to constrain. To find the atom numbers, open your structure in gaussview and select the atoms you want to constrain. The atom numbers will appear in the bottom left corner. Lastly, on the same line add the constrain option you would like. There are two main options, the first is freezing (add "F" to end of the line, nothing else is needed), which keeps the geometric parameter constant for all geometry iterations. The second is scanning (add "S" to the end of the line), which will iteratively scan a geometric parameter by increasing it or decreasing it by a set amount for a number of steps. Immediately following the "S", two numbers are required, first is the total number of steps you want (i.e. 10) followed by the amount you want to change the geometric parameter (i.e. 0.1). Examples of constraints for freezes and scans is below:

B 1 2 F --> freezes the bond between atoms 1 and 2 as defined in the xyz coordinates (check gaussview for atom numbers)

B 1 2 S 10 0.2 --> scans the bond between atoms 1 and 2, starting from the initial geometry in the .com file and increasing the bond length by 0.2 angstroms at each step. Since 10 steps are requested, with a step size of 0.2 angstroms, 11 (10+1, inclusive of first and last step) geometries will be generated starting from the inital structure and increasing the 1-2 BL out to +2 angstroms)

B 1 2 S 10 -0.2 --> scans the bond between atoms 1 and 2 in the reverse direction (i.e. reducing the bond length by 0.2 angstroms at each iterative step)

### Optional Keywords
Within the "opt" keyword, there are a number of optional modifiers that may aid your minimum geometry optimization. To use these, add them to the opt keyword in this way: ```opt=(OPTION1,OPTION2,OPTION3,...)```. Information for all options can be found here: [https://gaussian.com/opt/]
1. calcfc - This option calculates force constants for the molecule which can often speed up optimizations (more direct path to minimum can be found). This can be especially useful for shallow PESs (where large geometric changes result in small energetic changes)

## Analysis
1. Check the end of the ```.log``` file to confirm it has the line ```Normal Termination of Gaussian 16```, which confirms that the job finished successfully. If you do not have this line at the end of your file that means that the calculations failed (see common error messages to resolve this).
2. Open the ```.log``` file with GaussView. Right-click in the blue space to open the options and go down to "Results". Then click on "Vibrations...". This will bring up a box which shows the vibrational data of your molecule. You need to check that the frequencies for all modes are >0. This indicates that the electronic energy of the molecule increases in every direction on the highly dimensional PES (i.e. that the structure is a minimum).
    1. In the rare case that the minimum optimization generates one or more negative frequencies, choose the manual displacement option in the vibrations menu. Then move the slider to slightly change the molecule's geometry. Click "Save Structure..." and save this as a new ```.com/gjf``` file and submit another minimum optimization.
3. Next, open the ```.log``` file in bash and type ```/```. This does a forward search (like ctrl+f) of the file.
4. In some cases, the optimization plot can be important. This is a plot of each iterative geometry and its electronic energy. To open this plot, right-click on the blank space, go to results, then click on "Optimization...". Ideally this graph shows an exponential decrease in energy, until no further decrease occurs (convergence), though don't panic if it looks different or jagged. This plot can be especially useful in diagnosing errors when they arise. 

