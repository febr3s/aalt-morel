import pandas as pd
  
# reading the csv file
df = pd.read_csv("_data/booksa.csv")
  
# updating the column value/data
df = df.rename(columns={"File Attachments":"img"})

# writing into the file
df.to_csv("_data/booksa.csv", index=False)
  
print(df)