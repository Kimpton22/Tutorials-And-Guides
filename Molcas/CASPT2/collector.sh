#!/bin/bash
title='dbh-unsub'
> data.txt
for ((a=1;a<=500;a++))
do
log=$title-$a
cas_1=`grep -A1 'Total XMS-CASPT2 energies:' $log/$log.log|tail -n1|awk '{print $NF}'`
cas_2=`grep -A2 'Total XMS-CASPT2 energies:' $log/$log.log|tail -n1|awk '{print $NF}'`
cas_3=`grep -A3 'Total XMS-CASPT2 energies:' $log/$log.log|tail -n1|awk '{print $NF}'`
cas_4=`grep -A4 'Total XMS-CASPT2 energies:' $log/$log.log|tail -n1|awk '{print $NF}'`

osc_1=`grep -A10 'Dipole transition strengths (spin-free states)' $log/$log.log|grep '         1    2'|awk '{print $3}'`
osc_2=`grep -A10 'Dipole transition strengths (spin-free states)' $log/$log.log|grep '         1    3'|awk '{print $3}'`
osc_3=`grep -A10 'Dipole transition strengths (spin-free states)' $log/$log.log|grep '         1    4'|awk '{print $3}'`

printf "%s " $cas_1 >> data.txt
printf "%s " $cas_2 >> data.txt
printf "%s " $cas_3 >> data.txt
printf "%s " $cas_4 >> data.txt
printf "%s " $osc_1 >> data.txt
printf "%s " $osc_2 >> data.txt
printf "%s " $osc_3 >> data.txt
echo '' >> data.txt
done

