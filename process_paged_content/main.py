#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# main

from csv import DictReader
from json import dumps
from urllib import parse

from const import Const
from book import Book
from page import Page
from extractor import Extractor

def loop_pages(book, images):

		for page_num, page in enumerate(images):
			p = Page()
			if page_num is 0:
				p.write_page_headers()
			page_size = page._size
			# to prevent page = 0 
			page_num = page_num+1
			page_num = str(page_num)
			page.save(book.image_output_folder+'/page_'+page_num+'.jpg', 'JPEG')
			
			p.write_page_line(book.title, page_num, book.parent, book.issued_date)

			# details for iiif
			# label for page
			label = book.collection+"_"+book.parent+"_page_"+page_num+".jpg"
			url_encoded_label = parse.quote(label, safe='')
			# manifest id and "on"
			canvas_id = book.url+"/"+book.collection+"/"+book.parent+"/canvas/"+page_num
			# based on what's already in islandora node/x/manifest
			page_dict = {

				"@id": canvas_id,
				"@type": "sc:Canvas",
				"label": label,
				"height": page_size[0],
				"width": page_size[1],
				"images": [
				{
					"@id": book.url+"/"+book.collection+"/"+book.parent+"/annotation/"+page_num,
					"@type": "oa:Annotation",
					"motivation": "sc:painting",
					"resource": {
						"@id": book.url+"/cantaloupe/iiif/2/"+book.url_escaped+"%2F_flysystem%2Ffedora%2F"+book.migration_group+"%2F"+url_encoded_label+"/full/full/0/default.jpg",
						"@type": "dctypes:Image",
						"format": "image/jpeg",
						"height": page_size[0],
						"width": page_size[1],
						"service": {
							"@id": book.url+"/cantaloupe/iiif/2/"+book.url_escaped+"%2F_flysystem%2Ffedora%2F"+book.migration_group+"%2F"+url_encoded_label,
							"@context": "http://iiif.io/api/image/2/context.json",
							"profile": "http://iiif.io/api/image/2/profiles/level2.json"
						}
					},
					"on": canvas_id
				}
				]
			}
			book.starter_iiif['sequences'][0]['canvases'].append(page_dict)

			print("did page %s" % (page_num))
		print("finished book")
		iiif_json = dumps(book.starter_iiif)
		output_iiif_manifest = open(book.manifest_output_folder+book.parent+'.json','w')
		output_iiif_manifest.write(iiif_json)
		output_iiif_manifest.close()


# make me a const and all this
c = Const()

# read from csv
with open(c.collection_csv) as csv_file:

	csv_reader = DictReader(csv_file)

	for index, row in enumerate(csv_reader):

		# build book
		book = Book()
		if index is 0:
			book.write_book_and_manifest_headers()
		book.title = row['<mods:title>']
		# parent used often!
		book.parent = book.title.lower().replace(" ","_")
		book.subtitle=row['subtitle']
		book.description = row['description'] 
		book.extent = row['<mods:extent>'] # should be num_of_pages;type
		book.issued_date = row['<mods:dateCreated>']
		book.subjects = row['<mods:subject>']
		book.publisher = row['<mods:publisher>']
		book.geo_location = row['<mods:physicalLocation>']
		book.doi = row['<mods:identifier type="doi">']
		book.copyright = row['<mods:accessCondition type="">']
		book.language = row['<mods:language>']
		if book.language == "English":
			book.language="en"
		if row['type'] == "paged_content":
			hint = "paged"
		else:
			hint = "individual"

		# build start of iiif to be passed to extractor and written in Page
		pdf_file = 'pdfs/%s/%s' % ( book.collection, row['filename'] )

		

		book.starter_iiif = {
                "@context": "http://iiif.io/api/presentation/2/context.json",
                "@type": "sc:Manifest",
                "@id": book.url+"/"+book.collection+"/"+book.parent+"/manifest",
                "label": book.title,# maybe this could be different?
                "metadata":[
                    {'label':'Publisher', 'value':book.publisher},
                    {'label':'Published', 'value':[
                       {'@value':book.geo_location+', '+book.issued_date, '@language': book.language }
                      ]
                    }
                ],
                'description':book.description,
                'navDate':book.issued_date,
                'license':row['accessCondition_link'],
                "logo" : "https://www.library.cmu.edu/sites/drupal-live.library.cmu.edu/files/CMU_LibrariesLogo_Horizontal_Black.png",
                'attribution':book.copyright,
                "sequences":[{
                    "@context": "http://iiif.io/api/presentation/2/context.json",
                    "@id": book.url+"/"+book.collection+"/"+book.parent+"/sequence/normal",
                    "@type": "sc:Sequence",
                    "rendering": [
                      {
                        "@id": "https://dlcs.io/pdf/wellcome/pdf-item/b18035978/0",
                        "format": "application/pdf",
                        "label": "Download as PDF"
                      },
                      {
                        "@id": "https://wellcomelibrary.org/service/fulltext/b18035978/0?raw=true",
                        "format": "text/plain",
                        "label": "Download raw text"
                      }
                    ],
                    "viewingDirection": row['viewingDirection'],
                    "viewingHint": hint,
                    "behavior": [ "paged" ],
                    "canvases":[]
                }]
            }
		
		
		
		extractor = Extractor()
		book.image_output_folder = extractor.extract_pages(pdf_file,book.parent)
		loop_pages(book, extractor.images)
		book.write_book_node_line(book.parent)
		book.cleanup_ppms(book.image_output_folder)
		