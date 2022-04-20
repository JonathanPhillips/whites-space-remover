import pandas as pd

df = pd.read_csv('C:/example.csv') # read csv to dataframe

def whitespace_remover(dataframe):
     for i in dataframe.columns:
            if dataframe[i].dtype == 'object':
                    dataframe[i] = dataframe[i].map(str.strip)
            else:
                    pass

whitespace_remover(df)
print(df)  # print dataframe to console
df.to_csv('c:/example_clean.csv', index=False) # write the cleaned dataframe back to csv
