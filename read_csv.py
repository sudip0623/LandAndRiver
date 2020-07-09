import pandas as pd

def readcsv():
    file = pd.read_csv('Task_Training_Data .csv')

    # Getting the required fields
    result = file.iloc[:, lambda file: [0,1]]
    res = result.values.tolist()
    return res


