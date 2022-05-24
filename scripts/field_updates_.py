import pandas as pd
  
# reading the csv file
df = pd.read_csv("../assets/data/books_zotero.csv")
  
# updating the column value/data
df = df.rename(columns={"File Attachments":"Cover","Url":"Download","Library Catalog":"Library"})

# writing into the file
df.to_csv("../_data/books.csv")
  
print(df)