# Reading Intermediate Geometries
Reading of intermediate geometries is extremely important to view the iterative geometries that Gaussian generates during each job. By default this is turned off when you open an Gaussian output like a ```.log``` file. To turn this on, open GaussView, go to ```File``` then ```Open...```. Select the output file you would like to visualize, but before pressing open, check the box in the bottom right that says "Read Intermediate Geometries (Optimizations)". Once checked you will be able to see all iterative geometries that Gaussian generated, which is especially necessary for IRC and scan calculations, but it also necessary to view Optimization plots which can be useful when solving error messages. This only needs to be completed once, as this will be saved as your new default. 