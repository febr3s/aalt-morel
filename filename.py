for book in books:
	# converting the Authors column to an array
	author_raw = book[3]
	title_raw = book[4]
	# the next lines create the url part for for the main author
	authors_array = author_raw.split("; ")
	author_array = authors_array[0].split(", ")
	author = author_array[0]
	# the next lines create the different components of the url for the title
	title_raw = str(book[4]) 
	title_split = title_raw.split(" ")
	title_short = (title_split[:4])
	title = "-".join(title_short)

	year = str(book[2])

	url_raw = title+"-"+author+"-"+year
	
	url = slugify(url_raw) # slugify is an imported app