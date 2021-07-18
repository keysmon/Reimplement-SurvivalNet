# Reimplement-SurvivalNet

## The convert.py will load .mat format file and output .csv format files.
## Please make sure that the format of the mat input file is correct

### The expecting output of the convert.py will be:
1. Features.csv, which contains features table from the mat data.
2. Survival.csv, which contains Survival, AvailableClinical, AvailableCNV, AvailablemRNA, AvailableProtein, Censored tables from the mat data.
3. Symbols.csv, which contains Symbols, SymbolTypes data from the mat data.

### All tables are linked by a column named col_id.
