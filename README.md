# viral-evo-public
Code for SIR modeling of viruses.

# Basic usage

Compile with <code>make</code>
Create data files with the following format (you can also do this by running <code>python3 newsetup.py</code>)

## Region files:

Enter data file of the following form into <code>temp/region/REGION_NAME</code>, e.g. for <code>temp/region/usa</code>:
```
deathrate 0.0000211
birthrate 7000
initpop 330000000
```
deathrate = probability a given person in the USA dies on any given day (note that this is not age-stratified), birthrate = births per day, initpop = initial population 

## Disease files:

Enter data file of the following form into <code>temp/disease/DISEASE_NAME</code>, e.g. for <code>temp/disease/covid</code>:

```
virulence 0.00005503
sicklength 14
infectivity 0.000000000331
appearance 0
howmany 1000
```
virulence = increase in deathrate for infected population, sicklength = average length of infection, infectivity = P(X infects Y on day N) for any infected X, noninfected Y, and Day N, appearance = time disease appears (do <i>not</i> set this to be < 0), howmany = number of people infected when it appears
