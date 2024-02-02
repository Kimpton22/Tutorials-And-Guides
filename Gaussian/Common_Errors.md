# Common Error Messages and Solutions
Most errors in Gaussian end in the message: ```Error termination via Lnk1e```. This is the general "Oh no gaussian ran into a problem". Unfortunately, most gaussian error messages are not clear or easily diagnosable. Generally speaking, most gaussian jobs tend to fail due to a lack of convergence in either the SCF procedure (less common) or iterative geometries (more common). 

## Convergence failure -- maximum number of iterative geometries reached
For any geometry optimization to converge (whether to a minimum, TS, or on an excited state), the change in energy between iterative geometries needs to be quite small (<~10<sup>-7</sup>). If this convergence criteria is not met, then Gaussian will continue to iterate the geometry until convergence is met or a certain threshold of iterations is reached. This threshold is based on the size of the molecule, but has a minimum value of 20 iterations. Nonetheless, many jobs, especially ones which have exotic electronic structures or if a poor input geometry was provided, can run into this threshold. 

### Solving this issue
First, always check the optimization plot and scan through the iterative geometries, as this can often indicate the issue the calculation ran into and/or provide new guess geometries that might converge with slightly different methods or keywords. Here are a few things to watch out for in the optimization plot:
1. Repetitive cycles (or repetitive zig-zags) in the optimization plot: The iterative process sometimes gets stuck in cycles, constantly shifting between 2 structures, where the true critical point on the PES is the averaged structure between these two repetitive geometries. This issue is most common with resonance stabilized structures, molecules with oxygen double bonds, and/or jobs with a large maxstep (even the default maxstep can cause this issue). To solve this issue you can try reducing the maxstep size, though there is no true guarantee that whatever stepsize you choose will yield the correct structure. Alternatively, you can manual alter the geometry to represent the averaged structure that Gaussian is trying to optimize to (i.e. find the geometric change between repetitive strucutres and average this geometric parameter to use as a new input).
2. 


This [https://docs.alliancecan.ca/wiki/Gaussian_error_messages] source has excellent documentation of the most common Gaussian error messages.

## Other errors and possible solutions

