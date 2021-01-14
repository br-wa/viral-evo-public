# viral-evo-public
Code for SIR modeling of viruses and related scipts

# Dependencies 

C++: C++17, edit Makefile to use with C++11 or older versions
Python: The following packages <code>numpy, pandas, pathlib, decimal, matplotlib.pyplot, math</code>
R: The following libraries: <code>ggmuller, ggplot2</code>

# Basic usage

Set up the following subdirectories: <code>mullerplots</code>, <code>phaseplot</code>, <code>temp/disease</code>, <code>temp/region<code>
Compile with <code>make</code>
Create data files with the format specified below (you can also do this by running <code>python3 newsetup.py</code>)
Run <code>./sir REGION_NAME DAYS_TO_SIMULATE DISEASE1 DISEASE2 ... </code>, e.g. <code>./sir uk 400 covid_orig covid_b117</code> to produce output in raw CSV format (pipe with <code> > output.csv</code> for optimal use)

# Auxiliary code and visualizations

#### Muller plots:

After running <code>.sir</code> <b>and piping output to output.csv</code>, run <code>python3 mullerplot.py "title of graph" DISEASE1 DISEASE2</code>. This will output to a file in the <code>mullerplots</code> directory.

#### Phase diagrams:

Run <code>python3 phase.py</code> with the appropriate parameters. Note that <b>many features, including simulation length and the fact that there are only two viruses</code> are hard-coded. Edit the file at your own risk.

# Data formats

#### Region files:

Enter data file of the following form into <code>temp/region/REGION_NAME</code>, e.g. for <code>temp/region/usa</code>:
```
deathrate 0.0000211
birthrate 7000
initpop 330000000
```
deathrate = probability a given person in the USA dies on any given day (note that this is not age-stratified), birthrate = births per day, initpop = initial population 

#### Disease files:

Enter data file of the following form into <code>temp/disease/DISEASE_NAME</code>, e.g. for <code>temp/disease/covid</code>:

```
virulence 0.00005503
sicklength 14
infectivity 0.000000000331
appearance 0
howmany 1000
```
virulence = increase in deathrate for infected population, sicklength = average length of infection, infectivity = P(X infects Y on day N) for any infected X, noninfected Y, and Day N, appearance = time disease appears (do <i>not</i> set this to be < 0), howmany = number of people infected when it appears
