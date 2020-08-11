#/bin/bash

###### 
# to be done:
# - incorperate pdfminer library to extract text 
### ^ -- could use that for images
# - read metadata from csv
# - break out variables in to different file to make this more legible
# - move things in to functions to create legibility


import os
import json
from urllib import parse
from pdf2image import convert_from_path

#consts
url = "http://islandora-dev.library.cmu.edu:8000"
url_escaped = parse.quote(url, safe='')
collection = "thistle"
collection_pretty = "Thistle Yearbooks"
migration_group = "migrate_thistle"

# paged constants for descriptions etc.
book_title = ""
book_subtitle=""
book_description = "" 
book_extent = "" # should be num_of_pages;type
book_issued_date = ""
subjects = ""
author = ""
geo_location = ""
book_file = ""

#"Thistle %s|Thistle year book for %s||%s|%s pages;book|%s-01-01T00:00:00|College Yearbooks|Carnegie-Mellon University|Carnegie-Mellon University|%s_thistle\n") 

page_parent =""
page_description = ""
page_weight = ""

page_file_title = ""
page_file_subtitle = ""
page_file_description = ""
page_file_issued = ""

 
# assumes that all pdfs are in this dir and labeled as TYB_1982_0001.pdf
files = os.listdir('.')

output_page_files_csv = open(collection + '_page_files.csv','w')
output_page_files_csv.write('title|subtitle|description|issued|file\n')
output_page_nodes_csv = open(collection + '_page_nodes.csv','w')
output_page_nodes_csv.write('title|subtitle|description|parent|issued|weight|file\n')
output_book_nodes_csv = open(collection + '_book_nodes.csv','w')
output_book_nodes_csv.write('title|subtitle|description|collection|extent|issued|subjects|author|geo_location|file\n')

for file in files:
    if file[len(file)-3:len(file)] == 'pdf': # only continue if file is pdf
            # get year
            year = str(file[4:8])
            print(year)
            images = convert_from_path('./'+file, 125, './')
            print("doing it")
            # figure # of pages
            num_of_pages = len(images)
            print(str(num_of_pages) + " pages in year " + year)
            if num_of_pages == 0:
                print("skipping")
                continue

            # write book line
            book_line = ("Thistle %s|Thistle year book for %s||%s|%s pages;book|%s-01-01T00:00:00|College Yearbooks|Carnegie-Mellon University|Carnegie-Mellon University|%s_thistle\n") % (year,year,collection,str(num_of_pages),year,year)
            output_book_nodes_csv.write(book_line)
            starter_iiif_dict = {
                "@type": "sc:Manifest",
                "@id": "http://islandora-dev.library.cmu.edu:8000/"+collection+"/"+year+"/manifest",
                "label": "IIIF Manifest",
                "@context": "http://iiif.io/api/presentation/2/context.json",
                "sequences":[{
                    "@context": "http://iiif.io/api/presentation/2/context.json",
                    "@id": "http://islandora-dev.library.cmu.edu:8000/"+collection+"/"+year+"/sequence/normal",
                    "@type": "sc:Sequence",
                    "canvases":[]
                }]
            }

            for page_num, page in enumerate(images):
                page_num+=1
                page_num=str(page_num)
                # this is going to be a tuple of (height,width)
                page_size = page._size
                print(page_size)

                #save the page
                page.save('./images/thistle_'+year+'_page_'+page_num+'.jpg', 'JPEG')
                # write to page nodes and files
                node_line = ("Thistle %s page %s|||%s_thistle|%s-01-01T00:00:00|%s|%s/thistle_%s_page_%s.jpg\n") % (year,page_num,year,year,page_num,year,year,page_num)
                output_page_nodes_csv.write(node_line)

                file_line = ("Thistle %s page %s|||%s-01-01T00:00:00|%s/thistle_%s_page_%s.jpg\n") % (year,page_num,year,year,year,page_num)
                output_page_files_csv.write(file_line)
                # label for page
                label = collection+"_"+year+"_page_"+page_num+".jpg"
                url_encoded_label = parse.quote(label, safe='')
                # based on what's already in islandora node/x/manifest
                page_dict = {

                        "@id": url+"/"+collection+"/"+year+"/canvas/"+page_num,
                        "@type": "sc:Canvas",
                        "label": label,
                        "height": page_size[0],
                        "width": page_size[1],
                        "images": [
                            {
                            "@id": url+"/"+collection+"/"+year+"/annotation/"+page_num,
                            "@type": "oa:Annotation",
                            "motivation": "sc:painting",
                            "resource": {
                                "@id": url+"/cantaloupe/iiif/2/"+url_escaped+"%2F_flysystem%2Ffedora%2F"+migration_group+"%2F"+url_encoded_label+"/full/full/0/default.jpg",
                                "@type": "dctypes:Image",
                                "format": "image/jpeg",
                                "height": page_size[0],
                                "width": page_size[1],
                                "service": {
                                    "@id": url+"/cantaloupe/iiif/2/"+url_escaped+"%2F_flysystem%2Ffedora%2F"+migration_group+"%2F"+url_encoded_label,
                                    "@context": "http://iiif.io/api/image/2/context.json",
                                    "profile": "http://iiif.io/api/image/2/profiles/level2.json"
                                }
                            },
                            "on": url+"/"+collection+"/"+year+"/canvas/"+page_num
                            }
                        ]
                }
                starter_iiif_dict['sequences'][0]['canvases'].append(page_dict)
                print("done did a page")
            print("there you go, baby. end of a book!!!!!\n\n")
            iiif_json = json.dumps(starter_iiif_dict)
            output_iiif_manifest = open('thistle_manifest_'+year+'.json','w')
            output_iiif_manifest.write(iiif_json)
            output_iiif_manifest.close()

    else:
            continue

output_page_nodes_csv.close()
output_page_files_csv.close()
output_book_nodes_csv.close()

        
    

