import shutil
import os

import pandas as pd

from slugify import slugify

# Create a dataFrame from csv file
data = pd.read_csv("_data/booksa.csv", sep=',', engine ='python', encoding="utf-8").fillna('')

# Set the titles column to a list
books = data.values.tolist()

# Loop through each name, create .md file, set contents to string
for book in books:
	src = str(book[38])
	# the next lines create the different components of the url for the main author
	author_raw = str(book[13])
	author_split = author_raw.split(" ") # split is a built-in method, we are transforming the full name of the author into a list
	author_short = (author_split[-3:])
	author = "-".join(author_short)
	# the next lines create the different components of the url for the title
	title_raw = str(book[0]) 
	title_split = title_raw.split(" ")
	title_short = (title_split[:4])
	title = "-".join(title_short)

	year = str(book[3])

	url_raw = title+"-"+author+"-"+year
	
	file_name_slug = slugify(url_raw) # slugify is an imported app	

	file_name = str(file_name_slug)+".jpg"

	path = 'assets/img/'

	dst = path + file_name

	print(shutil.copyfile(src, dst))
