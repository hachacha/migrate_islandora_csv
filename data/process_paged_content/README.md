planning for this process
needs

### before

	- set up local CONST variables
	- move pdfs to islandora-file-staging 
	- create proper path named by collection that will be referenced within this doc

### during

	- read (loop) csv MODS file
		- what is the filename of X
		- per-item variables (subjects, page#, authors, etc.)
	- extract text from pdf
		- *should have a method for running this separately to test on*
	- extract jpegs from pdf
		- title and save them based the local CONST + the page#
	- create the csv for migration
		- collection, page files, page nodes, page media, book nodes, text files, and text media

### after / troubleshooting
	
	- tbd