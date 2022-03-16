# OPRA Simulations

This respository contains the workflow for the UW-Madison contribution to the
OPRA project. The current input files allow for an EG01 analysis and an
EG01-->23 transition analysis. 

Cyclus takes simulation inputs in the form of python dictionaries, and unlike
much previous work (done in XML), this project is converted to python for
simplified (to me) automation tasks.

While care was taken to follow the deployments for the FCO studies, this differs
in that it uses Cyclus' growth region to attain power demands versus manually
determined reactor deployments that optimize parameters important to that work.
The basics of the simulations in this work uses prototypes from the following
repositories: Baptiste Mouginot's [EG work for
FCO](https://github.com/bam241?tab=repositories&q=EG&type=&language=&sort=) and
U of Illinois ARFC's [transition
studies](https://github.com/arfc/transition-scenarios).

## input

This directory contains the scripts that create a suite of input files for the
simulations of interest for the OPRA project. 

The simulations are run from the notebook `inputs.ipynb`. The facilities and
recipes are saved in files that describe their use. The input files are also
saved as `[user_description].py` in this directory.

## output

The simulation databases should all be housed here because the analysis
directory relies on this file structure. Currently this is not part of the
repository since `*.sqlite` are git-ignored.

## analysis

This contains jupyter notebooks that process the simulation output for the EG
scenarios and parameter variations. 
