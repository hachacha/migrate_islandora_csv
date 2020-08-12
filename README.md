1. this should exist on both the target islandora server and on the file staging server
2. run process_paged_content portion on the file staging server (more details within that folder) - this generates the images, csvs, manifests, and (not right now) text files of the paged content.
3. commit the csvs that were generated and push
4. pull on the islandora server
5. run the migration from there

most variables can be changed within the const.py (like dpi, naming, etc) file in process_paged_content