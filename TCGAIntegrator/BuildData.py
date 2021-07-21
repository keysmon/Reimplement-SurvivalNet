from tcgaintegrator.BuildDataset import BuildDataset
import sys

Output = './'
FirehosePath = None
CancerCensusFile = None
MutsigQ = 0.1
GisticQ = 0.1

if(len(sys.argv) > 1):
    Diseases = sys.argv[1:]
else:
    Diseases = ["GBM","LGG","KIPAN"]
    #Diseases = ["BRCA","GBM","LGG","KIPAN"]
for Disease in Diseases:
    BuildDataset(Output, FirehosePath, Disease, CancerCensusFile, MutsigQ, GisticQ)
