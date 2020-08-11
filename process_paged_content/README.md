There are probably more things but just getting this up

### before

	- set up local CONST variables
	- move pdfs to islandora-file-staging 

### during

	- read (loop) csv MODS file
	- extract text from pdf
	- extract jpegs from pdf
	- create the csv for migration
		- collection, page files, page nodes, page media, book nodes, text files, text media, manifests

### after / troubleshooting
	
	- copy images to html folder
	- commit changes to this so the csvs are captured
	- pull on the islandora server
	- run migration from there.