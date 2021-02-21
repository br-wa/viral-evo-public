# viral-evo-public
Code for SIR modeling of viruses and related scipts

# Basic usage

<ol>
  <li> Set up the following subdirectories: <code>mullerplots</code>, <code>phaseplot</code>, <code>temp/disease</code>, <code>temp/region</code> </li>
  <li> Compile with <code>make</code> </li>
  <li> Create data files with the format specified below (you can also do this by running <code>python3 newsetup.py</code>) </li>
  <li> Run <code>./sir REGION_NAME DAYS_TO_SIMULATE DISEASE1 DISEASE2 ... </code>, e.g. <code>./sir uk 400 covid_orig covid_b117</code> to produce output in raw CSV format (pipe with <code> > output.csv</code> for optimal use) </li>
</ol>

# Auxiliary code and visualizations

#### Muller plots:

After running <code>./sir</code> <b>and piping output to <code>output.csv</code></b>, run <code>python3 mullerplot.py "title of graph" DISEASE1 DISEASE2</code>. This will output to a file in the <code>mullerplots</code> directory.

#### Phase diagrams:

Run <code>python3 phase.py</code> with the appropriate parameters. Note that <b>as written,  you must have a virus called "control" and one called "variable" (with specified sicklength, appearance, howmany parameters)</b>. Furthermore, <b>many features, including simulation length and the fact that there are only two viruses</code> are hard-coded. Edit the file at your own risk</b>. 

Similarly <code>phasemult.py</code> adapts <code>phase.py</code> to run with more than two viruses. However, its visualizations are not as useful due to them still being two-colored.

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

#### Output:

The output of <code>./sir</code> is in a <code>csv</code> format, with the following four global columns:
<ul>
  <li> <code>date</code>, the number of days since the start of the pandemic.</li>
  <li> <code>total infected</code>, the total number of people infected <b>at that point in time</b>.</li>
  <li> <code>total daily infections</code>, the number of people who were first infected <b>on that date</b>.</li>
  <li> <code>total recovered</code>, the cumulative number of people who have recovered from any of the diseases. </li>
</ul>
Furthermore, for each disease with name <code>[disease name]</code> we have the following three columns:
<ul>
  <li> <code>daily [disease name] infected</code>, the number of people who were first infected by the given disease on the specified date.</li>
  <li> <code>total [disease name] infected</code>, the total number of people infected by the given disease <b>at that point in time</b>.</li>
  <li> <code>[disease name] recovered</code>, the total number of people who recovered from the given disease.</li>
</ul>
Note that there is no label for total number of people who were ever infected. The number of recovered, however, is a good approximation for diseases with low virulence.
