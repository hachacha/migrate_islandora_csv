#/usr/bin/python
# run this after the recursivepdf2jpg.py file.
output_csv = open('thistle_page_files.csv','w')
import os
year_list = os.listdir('images')
for year in year_list:
	num_of_pages = len(os.listdir('./images/'+year))
	print(str(num_of_pages) + " pages in year " + year)
	if num_of_pages == 0:
		print("skipping")
		continue
	# create the csv based on num of pages for each year.
	for i in range(num_of_pages+1):
		if i is 0:
			continue
		# print(i)
		page = str(i)
		year = str(year)


		# print("/var/www/html/drupal/web/modules/contrib/migrate_islandora_csv/data-cmu/images/thistle/%s/page_%s.jpg,thistle %s page %s,,page %s of thistle %s,%s,") % (year,page,year,page,page,year,year)
		# print("Paged/%s_THISTLE,Paged/%s_THISTLE/%s,%s,/var/www/html/drupal/web/modules/contrib/migrate_islandora_csv/data-cmu/images/thistle/%s/page_%s.jpg") % (year,year,page,page,year,page)	
		line = ("%s_thistle|thistle/images/%s/thistle_%s_page_%s.jpg|thistle %s page %s||page %s of thistle %s|%s|%s\n") % (year,year,year,page,year,page,page,year,year,page)
		output_csv.write(line)


output_csv.close()
