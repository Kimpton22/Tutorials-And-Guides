# Common Error Messages and Solutions
Most errors in Gaussian end in the message: ```Error termination via Lnk1e```. This is the general "Oh no gaussian ran into a problem". Unfortunately, most gaussian error messages are not clear or easily diagnosable. Generally speaking, most gaussian jobs tend to fail due to a lack of convergence in either the SCF procedure (less common) or iterative geometries (more common). 

## Convergence failure -- maximum number of iterative geometries reached
For any geometry optimization to converge (whether to a minimum, TS, or on an excited state), the change in energy between iterative geometries needs to be quite small (<10<sup>-7)


This [https://docs.alliancecan.ca/wiki/Gaussian_error_messages] source has excellent documentation of the most common Gaussian error messages.

## Other errors and possible solutions

