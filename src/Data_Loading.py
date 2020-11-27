import os
path_parent = os.path.dirname(os.getcwd())


def load_district_data(file, column):
    import pandas as pd
    dataframe = pd.read_csv(path_parent + "/data/raw/" + file + ".csv")
    # keep only necessary columns
    dataframe = dataframe[column]
    return dataframe


def load_locality_data(file):
    import pandas as pd
    dataframe = pd.read_csv(path_parent + "/data/raw/" + file + ".csv")
    return dataframe

