# Installing Pyflow 

#### Reference VERDE Paper: https://pubs.acs.org/doi/10.1021/acs.jpclett.9b02577
This Github page contains instructions for installing Pyflow: 
```
https://github.com/northeastern-rc/pyflow-installation-script
```

### Reminders:
- Make sure to have PyFlow.txt in the same directory as install_pyflow.sh.
- If you have not loaded Gaussian and GAMESS on your .bashrc, you must uncomment lines 58 to 66 in the install_pyflow.sh file

### Testing installation
Copy necessary scripts:
```
cp -r /work/lopez/share_from_Leticia/test-pyflow/ .
```

#### Test 1 - Creating molecules
```
python pymolgen-bench.py bench-MB 'CN(C1=CC=C(N=C2C=C([U])C(N(C)C)=CC2=[S+]3)C3=C1)C'
```

#### Test 2 - Set up Workflow
```
pyflow setup bench_round001 --config_file config-001.json
```

#### Test 3 - Submit Workflow
```
cp bench-MB/* bench_round001/unopt_pdbs/ cd bench_round001/ && pyflow begin --do_not_track
```

#### Test 4 - Check progress
```
pyflow progress
```
--- 

# Generating Molecules
#### Copy pymolgen script from VERDE
```
cp /work/lopez/share_from_Leticia/verde-pyflow/pymolgen.py .
```

### Draw molecule on Chemdraw and select substituent location by using U for spacers




# Clean up workflow
Remove temporary files for failed jobs, for completed jobs them are automatically deleted
```
rm -r workflow*/*/*/failed/*.chk
```
```
rm -r workflow*/*/*/failed/*.rwf
```

## Extract results from Workflow using gather-results-withsp.py
1. Activate pyflow
```
conda activate pyflow
```
2. Run extraction script
```
python3 gather-results-withsp.py name-workflow
```

## Generate plots
### S0 Potentials + ColorMap showing wavelength
CSV details
  1. Need to be named S0.csv
  2. Collumn must have specific names: Oxi_S0,Red_S0,Wavelength

Usage
```
python3 plot-s0-colormap.py S0
```

Resulted plot
![plot_S0](https://github.com/adaogomesl/Leticia-LopezLab/assets/100699955/2a48e439-f486-4e13-8054-7ffd50c43fbd)

### Excited State Potentials + ColorMap showing wavelength
CSV details
  1. Need to be named S1.csv or T1.csv
  2. Collumn must have specific names: Oxi_S1,Red_S1
     
_in case of T1, replace S1 for T1_

Usage
```
python3 plot-scatter.py S1
```
Resulted plot
![plot_S1](https://github.com/adaogomesl/Leticia-LopezLab/assets/100699955/91ecc5c8-9702-404a-8524-cc4ce6e13bf2)
