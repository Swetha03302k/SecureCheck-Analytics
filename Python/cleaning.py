#Importing Libraries
import pandas as pd

#Read the dataset into a pandas dataframe
df = pd.read_excel(r"Data\traffic_stops.xlsx")

#Display the shape of the dataset before cleaning
print("Shape before cleaning:")
print(df.shape)

#Remove columns with all missing values
df.dropna(axis=1, how='all', inplace=True)

#Display the shape of the dataset after removing empty columns
print("Shape after removing empty columns:")
print(df.shape)

#Check for missing values
print("Missing values:")
print(df.isnull().sum())

#Handle missing values
print("Missing values in driver_age:")
print(df[['driver_age', 'driver_age_raw']].isnull().sum())

#Check missing values in categorical columns
print("Missing values in categorical columns:")
print(df[['driver_gender', 'driver_race', 'violation']].isnull().sum())

#Verify the missing values again
print(df.isnull().sum())

#Remove duplicate records
print("Duplicates Before:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Duplicates After:", df.duplicated().sum())

#Standardize categorical values
df['driver_gender'] = df['driver_gender'].replace({
    'M': 'Male',
    'F': 'Female'
})

print(df.dtypes)

#Save the cleaned dataset
df.to_csv(r"Data\traffic_stops_cleaned.csv", index=False)
print("Cleaned dataset saved successfully.")