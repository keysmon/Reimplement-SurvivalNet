from scipy.io import loadmat
import pandas as pd
import numpy as np
import sys

def mat2csv(file_mat, index=False):
    try:
        mat = loadmat(file_mat)
    except:
        sys.stderr.write("convert.py -> Fatal Error: Cannot open file\n")
        exit(1)

    data = {}
    data['col_id'] = []
    for col_id in range(len(mat['AvailableClinical'][0])):
        data['col_id'].append(col_id)


    data['AvailableClinical'] = []
    for row in mat['AvailableClinical']:
        for col_id, value in enumerate(row):
            if value == "Yes":
                data['AvailableClinical'].append(1)
            else:
                data['AvailableClinical'].append(0)

    data['AvailableCNV'] = []
    for row in mat['AvailableCNV']:
        for col_id, value in enumerate(row):
            if value == "Yes":
                data['AvailableCNV'].append(1)
            else:
                data['AvailableCNV'].append(0)

    data['AvailablemRNA'] = []
    for row in mat['AvailablemRNA']:
        for col_id, value in enumerate(row):
            if value == "Yes":
                data['AvailablemRNA'].append(1)
            else:
                data['AvailablemRNA'].append(0)

    data['AvailableProtein'] = []
    for row in mat['AvailableProtein']:
        for col_id, value in enumerate(row):
            if value == "Yes":
                data['AvailableProtein'].append(1)
            else:
                data['AvailableProtein'].append(0)

    data['Censored'] = []
    for row in mat['Censored']:
        for col_id, value in enumerate(row):
            data['Censored'].append(value)

    data['Survival'] = []
    for row in mat['Survival']:
        for col_id, value in enumerate(row):
            data['Survival'].append(value)



    df = pd.DataFrame(data)


    data1 = {}
    for col_id in range(len(mat['Features'][0])):
        data1[col_id] = []

    for row in mat['Features']:
        for col_id, value in enumerate(row):
            data1[col_id].append(value)

    df1 = pd.DataFrame(data1)



    data2 = {}
    data2['col_id'] = []
    for col_id in range(len(mat["Symbols"])):
        data2['col_id'].append(col_id)

    data2["Symbols"] = []
    for row in mat['Symbols']:
        data2["Symbols"].append(row)

    data2["SymbolTypes"] = []
    for row in mat['SymbolTypes']:
        data2["SymbolTypes"].append(row)

    #print(data2["Symbols"])
    df2 = pd.DataFrame(data2)
    

    df3 = np.concatenate((df2, df1), axis=1)
    df3 = pd.DataFrame(df3)
    #df3 = pd.DataFrame(data1, columns = data2["Symbols"])
    df3 = df3.T
    df3.drop(df3.index[2], inplace=True)
    df3.columns = df3.iloc[1]
    df3 = df3[2:]

    df3['Survival'] = df['Survival']
    df3['AvailableClinical'] = df['AvailableClinical']
    df3['AvailableCNV'] = df['AvailableCNV']
    df3['AvailablemRNA'] = df['AvailablemRNA']
    df3['AvailableProtein'] = df['AvailableProtein']
    df3['Censored'] = df['Censored']
    df3['Survival'] = df['Survival']
    
    #print(df3.shape)
    df3.to_csv("Survival.csv", index=index)

    

def main():
    if(len(sys.argv) != 2):
        sys.stderr.write("convert.py -> Fatal Error: Missing input .mat file\n")
        exit(1)
    file = sys.argv[1]
    mat2csv(file)



if __name__ == "__main__":
    main()
