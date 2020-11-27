# Importing the libraries
import pandas as pd
import numpy as np
import ast
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import sqlalchemy
import configparser
import os
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from six.moves import urllib
from Data_Loading import load_district_data, load_locality_data
from Calculations import total_enrollments, pct_subgroup
from dotenv import load_dotenv
load_dotenv(verbose=True)


path_parent = os.path.dirname(os.getcwd())
"""Load configuration from .ini file."""
# Read local file `config` file.
config = configparser.ConfigParser()
config.read(path_parent + '/Config.ini')
column_names = config.get("Col_to_keep", "column_names")
column_names = ast.literal_eval(column_names)

warnings.filterwarnings('ignore')
imp = IterativeImputer(max_iter=10, random_state=0)
scaler = StandardScaler()

# Reading the district dataset
data = load_district_data("district_dataset_200521", column_names)
locale = load_locality_data("locale")

# Calculate the total enrollments and remove  the grade wise columns
data = total_enrollments(data)

# Merge the district locale in this data
data = pd.merge(data, locale, on='leaid', how='left')
data = data.drop(["locale"], axis=1)

# Drop the School Districts with not recorded enrollments and Total Enrollments recorded "0"
data = data.dropna(subset=['Total_Enrollment'])
data = data[data.Total_Enrollment != 0]
data = data.reset_index(drop=True)
data = data.rename(columns={"locale2": "District_Locale"})  # Rename the column
# Convert categories of District Locale to Distance Measures
data.District_Locale = data.District_Locale.replace(['City', 'Town', 'Suburban', 'Rural'], [1, 2, 3, 4])

# Call the pct_subgroup function
data = pct_subgroup(data)

# Impute nulls using multivariate feature imputation
df = data[['leaid', 'statename', 'lea_name']]
data = data.drop(['leaid', 'statename', 'lea_name'], axis=1)
df2 = imp.fit_transform(data)
df2 = pd.DataFrame(df2)
df2.columns = data.columns
data = pd.concat([df, df2], axis=1)

# Remove the subgroup enrollments columns
data = data.drop(columns=["American_Indian", "Asian", "Black_or_African_American", "Hispanic_or_Latino", "Hawaiian",
                          "Not_Specified", "Multi_Racial", "White"])

data.to_csv(path_parent + "/data/interim/Algo_Input_Data.csv", index=False)  # File is ready to input to Algorithm
print(data.shape)

feature_column = ['operational_schools', 'Total_Enrollment', 'District_Locale', 'totalexp_1617',
                  'expps_1617', 'ell_1617_pct', 'American_Indian_pct', 'Asian_pct', 'Black_or_African_American_pct',
                  'Hispanic_or_Latino_pct', 'Hawaiian_pct', 'Not_Specified_pct', 'Multi_Racial_pct', 'White_pct']
# 'American_Indian', 'Asian', 'Black_or_African_American', 'Hispanic_or_Latino', 'Hawaiian',
# 'Not_Specified', 'Multi_Racial', 'White' Enrollments columns removed.

features = data[feature_column]  # Features data frame

# Scale the column values using standard scaler to obtain mean 0 and standard deviation 1
scaled = scaler.fit_transform(features)
scaled = pd.DataFrame(scaled)
scaled.columns = features.columns  # scaled data

# Calculate the Cosine Similarity
cosine_val = cosine_similarity(scaled)

# Iterate through 50 iterations at a time to speed up the iterations
final = pd.DataFrame()
ls = np.arange(0, 18000, 50).tolist()
ls[-1] = len(data)

# Get values from our .ini file
# Read environmental variables
load_dotenv(dotenv_path=path_parent + ".env")
Database = os.getenv("DATABASE")
Driver = os.getenv("DRIVER")
Server = os.getenv("SERVER")
Uid = os.getenv("UID")
password = os.getenv("PWD")

# To insert data frame into MS SQL database without iterate the data-frame
params = urllib.parse.quote_plus("DRIVER=" + Driver + ";SERVER=" + Server + ";DATABASE=" + Database + ";UID=" + Uid + ";PWD=" + password)
engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
engine.connect()

# Push the data to MS-SQL
for j in range(len(ls) - 1):
    output = pd.DataFrame()
    for i in range(ls[j], ls[j + 1]):
        print(i)
        df = pd.concat([data, pd.Series(cosine_val[i])], axis=1)
        df['leaid_match'] = data.leaid[i]
        output = output.append(df)
    final = final.append(output)
    final = final.reset_index(drop=True)
    final = final.rename(columns={0: "Similarity_Score"})
    final = final[['leaid', 'leaid_match', 'Similarity_Score']]
    if j == 0:
        final.to_sql(name="District_Like_Me", con=engine, index=False, if_exists='replace')
        final.to_csv(path_parent + "/data/processed/Sample_1.csv", index=False)
    else:
        final.to_sql(name="District_Like_Me", con=engine, index=False, if_exists='append')
    final = pd.DataFrame()
