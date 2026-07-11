import pandas as pd

#Read the dataset into a pandas dataframe
df = pd.read_excel(r"Data\traffic_stops.xlsx")

#Display first five records
print(df.head())

#Display last five records
print(df.tail())

#Check dataset dimensions
print(df.shape)

#Display column names
print(df.columns)

#Verify the data types
print(df.dtypes)

#Display dataset information
df.info()

#Display unique values
print(df.nunique())

#Generate summary statistics
print(df.describe())

#Verify the number of missing values in each column
print(df.isnull().sum())

#Check duplicate records
print(df.duplicated().sum())

#Display unique values in a specific column
print(df['country_name'].unique())

#Display unique values in a specific column
print(df['country_name'].value_counts())

#Check percentage of missing values in each column
print((df.isnull().sum()/len(df))*100)

#Display unique values in a specific column
print(df['driver_gender'].unique())
print(df['driver_race'].unique())
print(df['violation'].unique())
print(df['search_type'].unique())
print(df['stop_outcome'].unique())