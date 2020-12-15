# background

cmu-specific workflow and migration of archivalware items in to islandora

## steps for metadata workers

### the headers don't really matter that much for Islandora but we have decided to go with MODS as it's most comfy for our purposes.

1. clean the metadata
	a) make sure all relevant fields are represented
	b) normalize the dates -- if possible convert to iso 8601
2. put that mods csv file in to `/proces_paged_content` 
3. any subjects, keywords, creators, corporate bodies, etc. -- things that have an authority file on LOC -- should be put in to the corresponding csv in `/data/taxonomy/`
	a) if you have a whole lot of subjects that do not have authority files associated we can run them in loc_af_search and get those -- ask jon
	b) headers are different depending on type of taxonomy term
4. review this with your dev. it's important they understand what data is going in and how it should be organized
	a) you may need to rename the files so they match some sort of identifier
	b) you may need to come up with a common identifier throughout. see _cmu migration style conventions_ below

## running for dev

1. this repo should exist on both the target islandora server and on the file staging server

*! make sure you check the style conventions!*

2. update the yml files for the specific data being transferred in `config/install/migrate_plus.migration.COLLECTION...yml`
2. run process_paged_content portion on the file staging server _more details within that folder_ . it will:
	a) read through the MODS csv, 
	b) generates the images from pdfs, 
	c) create migration csvs, text files, and manifests for the `/data` folder
3. commit the csvs that were generated and push
4. pull on the islandora server
5. uninstall and reinstall with drush 
6. run the migration from there




# cmu migration style conventions

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


## taxonomy

	- should run the majority first and then run an --update in order link items together with `parent` & `related-entities`
	- place all in data/taxonomy/cmu_taxonomy_name_of_vocabulary_name.csv
	- keep it plural