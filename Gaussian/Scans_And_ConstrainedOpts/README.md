# 1. Scans and Constrained Optimizations
Constrained optimizations and scans in gaussian look to minimize the energy of a structure by varying geometric parameters in the molecule, within the bounds of user-defined constraints. Constrained optimizations are useful to freeze certain critical geometric parameters while allowing the rest of the structure to relax into a better geometry. Scans are a series of constrained optimizations which iteratively increase or decrease on one (1D) or two (2D; not recommended) geometric parameters. Scans are especially useful to get a rudimentary idea of the PES and search for TSs or maxima on the PES. Each chemical reaction requires some form of bond breakage, so the geometric parameters around this bonding change can be scanned to find a good guess for TSs. 
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
     1. It is not uncommon for constrained optimizations and especially scans to fail. In a lot of cases this is totally fine, as we are not looking for critical points on the PES, but instead getting a good starting point for further optimization. Even if the jobs ended in failure, continue onto step 2.
### Constrained Optimization
2. Open the ```.log``` file with GaussView. Visually inspect the structure to see if it adopted an acceptable geometry. If so, proceed with whatever calculation you want (usually an unconstrained TS or minimum optimization).
3. If the geometry does not look how you want or expect, check the optimization plot (right-click in the blue space to open the options and go down to "Results". Then click on "Optimization...") and look to see how the structure changed. Based on this you can re-submit a new constrained optimzation, modifying the constraints based on how the molecule relaxed. 
### Scans
2. Open the ```.log``` file with GaussView. Right-click in the blue space to open the options and go down to "Results", then click on "Scan..." to view the scanned geometries and their electronic energies. Often times we perform scans to find a TS on the PES. In this case, we are searching for a maximum on the scan. The geometry of the maximum point on the scan graph can be saved as a new structure to be submitted as a TS optimization.
3. In many cases, no maximum will be found and the energy will consistently increase or decrease. This can indicate a number of things:
    1.First, its possible that this is not the best geometric constraint to find the TS. Try scanning other geometric parameters which are related to the reaction.
    2. Second, many TSs require the movement of multiple geometric parameters. As one parameter is scanned the other geometric parameters will move to compensate, usually this is robust enough to find a maximum on the scan PES. However, for tricky reactions/TSs, it may be helpful to perform a 2D scan (where two geometric constraints are scanned). Every combination of BL/Angle/Dihedral will be tested (unless the job fails early), which means if you want to scan two bonds with 10 steps each, 100 (10*10) geometries and energies will be generated. If the job does not error out, gaussian will convert the scan plot into a 3D graph, but if any error occurs it treats the result as a 1D scan, which can be difficult to interpret. Generally speaking 2D scans are difficult to perform and should be avoided if at all possible.
    3. Lastly, there a numerous chemical reactions for which methods cannot calculate TSs (or maximums) for. A good example of this is the first step of an SN1 reaction, which is notoriously difficult to find TSs for with DFT especially. This mostly occurs for bond dissociations, especially with ionization like in the SN1 reaction. Another example of this is protonation/deprotonation steps, which you should not attempt to find TSs for. 

