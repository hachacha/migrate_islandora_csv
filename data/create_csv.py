#/usr/bin/python

for i in range(329):
	if i is 0:
		continue
	# print(i)
	year = "1982"
	page = i
	# print("/var/www/html/drupal/web/modules/contrib/migrate_islandora_csv/data-cmu/images/thistle/%s/page_%s.jpg,thistle %s page %s,,page %s of thistle %s,%s,") % (year,page,year,page,page,year,year)
	print("Paged/%s_THISTLE,Paged/%s_THISTLE/%s,%s,/var/www/html/drupal/web/modules/contrib/migrate_islandora_csv/data-cmu/images/thistle/%s/page_%s.jpg") % (year,year,page,page,year,page)