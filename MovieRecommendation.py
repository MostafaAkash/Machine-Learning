import numpy
import pandas as pd
import numpy as np
import warnings

a = numpy.random.randint(1,10,(10,5))
print(a)

warnings.filterwarnings('ignore')

#no need #df = pd.read_csv(r'c:/my_folder/some_other_folder/FremontBridge.csv', index_col='Date', parse_dates=True)
df = pd.read_csv(r'C:\Users\slowg\Desktop\Datasetm\data\ratings.csv',delimiter=',',names=['userId','movieId','rating','timestamp'])
#print(df)
print(df.head())

mv = pd.read_csv(r'C:\Users\slowg\Desktop\Datasetm\data\movies.csv',delimiter=',')

#movieTitles = mv['movieId','title']
fields = ['movieId','title']
movieTitles = pd.read_csv(r'C:\Users\slowg\Desktop\Datasetm\data\movies.csv',skipinitialspace=True,usecols=fields)


#print(movieTitles)
print(movieTitles.head())

#df = pd.merge(df,movieTitles,on='movieId')
#xy = pd.merge(df,movieTitles,how='outer')
#print(xy.head())

df1 = pd.DataFrame(df)
df2 = pd.DataFrame(movieTitles)
df1 = df1.convert_objects(convert_numeric=True)
df2 = df2.convert_objects(convert_numeric=True)

print(df1.dtypes)
print(df2.dtypes)

xy = pd.merge(df1, df2, on='movieId')
print(xy.head())

print(df.describe())
