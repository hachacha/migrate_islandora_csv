#/usr/bin/python

# run this after the recursivepdf2jpg.py file.

output_page_files_csv = open('thistle_page_files.csv','w')
output_page_files_csv.write('title|subtitle|description|issued|file\n')
output_page_nodes_csv = open('thistle_page_nodes.csv','w')
output_page_nodes_csv.write('title|subtitle|description|parent|issued|weight|file\n')
output_book_nodes_csv = open('thistle_book_nodes.csv','w')
output_book_nodes_csv.write('title|collection|subtitle|description|extent|issued|subjects|author|geo_location|file\n')

import os
year_list = os.listdir('images')
for year in year_list:
	num_of_pages = len(os.listdir('./images/'+year))
	print(str(num_of_pages) + " pages in year " + year)

	if num_of_pages == 0:
		print("skipping")
		continue
	
	# write to book node
	book_line = ("Thistle %s|thistle|Thistle year book for %s||%s pages;book|%s-01-01T00:00:00|College Yearbooks|Carnegie-Mellon University|Carnegie-Mellon University|%s_thistle\n") % (year,year,str(num_of_pages),year,year)
	output_book_nodes_csv.write(book_line)
	# create the csv based on num of pages for each year.
	for i in range(num_of_pages+1):
		if i is 0:
			continue

		page = str(i)
		year = str(year)

		
		# write to page nodes and files
		node_line = ("Thistle %s page %s|||%s_thistle|%s-01-01T00:00:00|%s|%s/thistle_%s_page_%s.jpg\n") % (year,page,year,year,page,year,year,page)
		output_page_nodes_csv.write(node_line)

		file_line = ("Thistle %s page %s|||%s-01-01T00:00:00|%s/thistle_%s_page_%s.jpg\n") % (year,page,year,year,year,page)
		output_page_files_csv.write(file_line)
	

output_page_nodes_csv.close()
output_page_files_csv.close()
output_book_nodes_csv.close()