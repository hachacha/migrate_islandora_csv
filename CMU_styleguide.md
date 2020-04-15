## naming conventions

	- everything in status should have explicit naming :
		- thistle_collection
		- thistle_1982_book_node    
		- thistle_1982_page_files   
		- thistle_1982_page_nodes   
		- thistle_1982_page_media   
	- migrations should be done in the above order. collections and books first so that the pages can go where they are supposed to. 
	-csvs and yml files should be named the same
	/data/thistle_1982_page_files.csv == /config/install/thistle_1982_page_files.yml

## configs
	
	- should try to fill as many fields as possible for metadata needs.

## CSVs in /data

	- identifier all lower case
	- title is used for the title for all entries instead of pagename/bookname/etc. 
	- all delimeters should be | (pipes)

### page nodes
	
	- title: collection, title, year, page# (thistle 1982 page 1)
	- i think it's best to have separated csvs for page nodes and page files uploading because the file elements will not require to have much metadata attached.

### media
	
	- if necessary should have it's own csv but in general it should share the same csv as _file. other metadata can live in the node
	- config files should really just state the relationship between file and nodes