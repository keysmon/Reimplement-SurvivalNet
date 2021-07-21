from scipy.io import loadmat
import pandas as pd


def mat2csv(file_mat, index=False):
    mat = loadmat(file_mat)

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
    df.to_csv("Survival.csv", index=index)

    data1 = {}
    for col_id in range(len(mat['Features'][0])):
        data1[col_id] = []

    for row in mat['Features']:
        for col_id, value in enumerate(row):
            data1[col_id].append(value)

    df = pd.DataFrame(data1)
    df.to_csv('Features.csv', index=index)

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

    df = pd.DataFrame(data2)
    df.to_csv("Symbols.csv", index=index)

def main():
    x = raw_input("Please enter mat file name: ")
    mat2csv(x)
    


if __name__ == "__main__":
    main()