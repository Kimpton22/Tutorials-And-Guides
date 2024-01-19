# 1. Scans and Constrained Optimizations
Ground state geometry optimizations in gaussian look to minimize the energy of a structure by varying geometric parameters in the molecule. It does this using first and sometimes second order derivatives. Geometry optimizations will continue until a) a stationary point is reached on the potential energy surface (PES) (stationary points includes TSs and minima) b) an error causes the job to end early or c) the maximum number of geometry iterations is reached.
## References
Opt keyword info: [https://gaussian.com/opt/] (see options and modredundant for more information on constrained optimizations specifically)


## Files necessary
```.com or .gjf and .sh (not necessary if using python submit script)```

## Keywords and Mandatory Set-up
There is one mandatory keyword for geometry optimizations which is ```opt=modredundant```. ```opt``` asks gaussian to do a geometry optimization (searching for a minimum energy structure by default) and the ```modredundant``` option signals to gaussian that there are geometric constraints. 

Constraints and scans are added to the bottom of the ```.com/gjf``` file, after all xyz coordinated. Make sure that there is exactly one blank line separating the xyz coordinates and the constraints. There is no limit on the number of constraints you can add, however adding too many constraints often leads to errors in gaussian, so limit them as much as possible. 

Any geometric parameter can be constrained or scanned. This include bond lengths, angles and dihedrals. Constraints are set first by indicating 
### Optional Keywords
Within the "opt" keyword, there are a number of optional modifiers that may aid your minimum geometry optimization. To use these, add them to the opt keyword in this way: ```opt=(OPTION1,OPTION2,OPTION3,...)```. Information for all options can be found here: [https://gaussian.com/opt/]
1. calcfc - This option calculates force constants for the molecule which can often speed up optimizations (more direct path to minimum can be found). This can be especially useful for shallow PESs (where large geometric changes result in small energetic changes)
2. maxstep=X - This option reduces or increases the maximum distance the procedure can move atoms between iterations. This useful for meta-stable intermediates which tend to collapse towards reactants or products. The default is 30 which corresponds to 0.3 bohr or radian units.

## Analysis
1. Check the end of the ```.log``` file to confirm it has the line ```Normal Termination of Gaussian 16```, which confirms that the job finished successfully. If you do not have this line at the end of your file that means that the calculations failed (see common error messages to resolve this).
2. Open the ```.log``` file with GaussView. Right-click in the blue space to open the options and go down to "Results". Then click on "Vibrations...". This will bring up a box which shows the vibrational data of your molecule. You need to check that the frequencies for all modes are >0. This indicates that the electronic energy of the molecule increases in every direction on the highly dimensional PES (i.e. that the structure is a minimum).
    1. In the rare case that the minimum optimization generates one or more negative frequencies, choose the manual displacement option in the vibrations menu. Then move the slider to slightly change the molecule's geometry. Click "Save Structure..." and save this as a new ```.com/gjf``` file and submit another minimum optimization.
3. Next, open the ```.log``` file in bash and type ```/```. This does a forward search (like ctrl+f) of the file.
4. In some cases, the optimization plot can be important. This is a plot of each iterative geometry and its electronic energy. To open this plot, right-click on the blank space, go to results, then click on "Optimization...". Ideally this graph shows an exponential decrease in energy, until no further decrease occurs (convergence), though don't panic if it looks different or jagged. This plot can be especially useful in diagnosing errors when they arise. 

