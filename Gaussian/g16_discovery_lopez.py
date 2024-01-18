#!/usr/bin/python

import sys
import os

##############################################
# Email Notification Settings                #
#                                            #
# Set "send_email" to 1 and edit your email  #
# address to enable email notification       #
#                                            #
# email_options:                             #
#   begin, end, fail, or all                 #
#                                            #

send_email = 0
email_address = "larmore.s@northeastern.edu"
email_options = "end,fail"

#                                            #
# End of Email Notification Settings         #
##############################################

l = len(sys.argv)
if l < 2:
  print('Usage: '+os.path.basename(sys.argv[0])+' filename.com ncpus(=16) walltime(=1day) memory(=16)')
  sys.exit(1)

walltime = "1"
ncpus = 16
mem = 16

if l >= 3:
  ncpus = int(sys.argv[2])

if l >= 4:
  walltime = sys.argv[3]

if l >= 5:
  mem = int(sys.argv[4])

def write_bash_file(bash_filename, g16_filename, filename):
    """
    Writes a bash file which is submitted to the queue. 
    bash_filename (string): name of the bash file to be created 
    g16_filename: Gaussian 16 input file
    """
    
    bash_file = open(bash_filename, "w")
    bash_file.write("#!/bin/bash\n")
    bash_file.write('#SBATCH --job-name='+g16_filename+'\n')
    bash_file.write('#SBATCH --input='+filename+'\n')
    bash_file.write('#SBATCH --partition=lopez\n')
    bash_file.write('#SBATCH --time='+str(walltime)+'-00:00:00\n')
    bash_file.write('#SBATCH --nodes=1\n')
    bash_file.write('#SBATCH --ntasks='+str(ncpus)+'\n')
    bash_file.write('#SBATCH --mem='+str(mem)+'Gb\n')
    bash_file.write('#SBATCH --output=%j.o.slurm\n')
    bash_file.write('#SBATCH --error=%j.e.slurm\n')

    bash_file.write('hostname\n')
    bash_file.write('export g16root=/work/lopez/\n')
    bash_file.write('. $g16root/g16/bsd/g16.profile\n')
    bash_file.write('work=`pwd`\n')
    bash_file.write('export GAUSS_SCRDIR=$WORKING_DIR\n')
    bash_file.write('cd $work\n')
    bash_file.write('time $g16root/g16/g16 '+filename)
    
    bash_file.close()

def main():  #submits bash file to queue.
   
    filename = sys.argv[1] 
    g16_filename = filename.split('.')[0]
    bash_filename = g16_filename+'.sbatch'
    write_bash_file(bash_filename, g16_filename, filename)
    os.system('sbatch '+bash_filename)
  
if __name__ == "__main__":
  main()
