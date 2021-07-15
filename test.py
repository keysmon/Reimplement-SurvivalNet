from tcgaintegrator.BuildDataset import BuildDataset

Output = '/Users/liqiaowang/Desktop/SENG474/project/TCGA_INTERGRATOR'
FirehosePath = None
Disease = 'LGG'
CancerCensusFile = None
MutsigQ = 0.1
GisticQ = 0.1
BuildDataset(Output, FirehosePath, Disease, CancerCensusFile, MutsigQ, GisticQ)