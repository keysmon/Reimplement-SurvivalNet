# Reimplement-SurvivalNet

We will try to reimplement the SurvivalNet project.  We will use data from the TCGA dataset, namely

| DiseaseName	| Code 		| 
| -------------	|-------------:| 
| Brain(pan-glioma) 	| LGG/GBM	| 
| LUNG 		| LUAD 		|
| Pan-kidney	| KIPAN		|

This project includes a virtual environment of the 2nd generation of python. All testing should be done in the virtual environment to maintain consistency

To create the virtual enviroment, make sure your pip is also the generation
check pip version by
```
>pip -V
```
install virtualenv
```
>pip install virtualenv
```

To init the virtual enviroment
```
>virtualenv Integrator
>source ./Integrator/bin/activate
>pip install requests
>pip install numpy
>pip install scipy
>pip install pandas
```

To activate the virtual enviroment, run
```
>source ./Integrator/bin/activate
```

The resource folder includes references to articles, sources, and the original paper.

The TCGA Integrator can generate the training data. But as of right now it cannot generate data for BRCA.

To run the TCGA Integrator and download the default dataset, run
```
>python BuildData.py
```

To run the TCGA Integrator with specific disease name, run
```
>python BuildData.py [Disease_name1] [Disease_name2] [Disease_name3] ... 
```
e.g
```
>python BuildData.py GBM KIPAN LGG
```

Github cannot store dataset of that size, so it's encouraged to run your own integrator and store the data at a local location

### data conversion
The convert.py will load .mat format file and output .csv format files.
### Please make sure that the format of the mat input file is correct

### The expecting output of the convert.py will be one file named Survival.csv
1. Each row represents one patient.
2. The name of symbols and censored are listed as column name.


## Please check the example_data.csv to see the example output of the convert.py.
