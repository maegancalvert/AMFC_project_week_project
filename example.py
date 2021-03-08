import pandas as pd
import numpy as np

fh = '/home/mcalvert/workspace/code/script_generation/SST_demographic_2021_Maegan_working.csv'
df = pd.read_csv(fh, delimiter=',')

### want to drop all rows and columns will all NaN
df.dropna(axis=0, how='all', inplace=True)
df.dropna(axis=1, how= 'all', inplace=True)
#df.set_index('Subject', inplace=True)
#print(df)

### find all participants who were not part of Amanda's study and drop the participants who were part of Amanda's study
#for i, row in df.iterrows(): #this is used to iterate over rows using the index (i), but not needed for this script
df2 = (df.where(df['In_Amanda_HBM_2014'] == 0))
df2.dropna(axis=0, subset=['In_Amanda_HBM_2014'], inplace=True)
#print(df2)

###find all participants who are older than age 17 and drop participants who are under the age of 18
df3 = (df2.where(df2['Age'] > 17))
df3.dropna(axis=0, subset=['Age'], inplace=True)

###find all participants who were part of the UAMS cohort and delete all participants who were part of the Emory cohort
df4 = (df3.where(df['Subject'] > 3200))
df4.dropna(axis=0, subset=['Subject'], inplace=True)

df4.to_csv('/home/mcalvert/workspace/code/script_generation/SST_demographic_2021_Maegan_revised.csv')
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df4.count())
print(df4.describe())
print(df4.groupby(['Sex']).count())
#print(sex_df)