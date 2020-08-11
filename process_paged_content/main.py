#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# main

import os
import csv
from urllib import parse
from const import Const
from book import Book
from page import Page
from extractor import Extractor


# make me a const and all this
c = Const()


# read from csv
with open(c.collection_csv) as csv_file:
	csv_reader = csv.DictReader(csv_file)
	line_count = 0
	for row in csv_reader:

		# build book
		book = Book()
		book.title = row['<mods:title>']
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
		print(pdf_file)
		parent = book.title.lower().replace(" ","_")
		starter_iiif = {
                "@context": "http://iiif.io/api/presentation/2/context.json",
                "@type": "sc:Manifest",
                "@id": book.url+"/"+book.collection+"/"+parent+"/manifest",
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
                "logo" : "https://www.library.cmu.edu/sites/drupal-live.library.cmu.edu/files/CMU_LibrariesLogo_Horizontal_Black.png"
                'attribution':book.copyright,
                "sequences":[{
                    "@context": "http://iiif.io/api/presentation/2/context.json",
                    "@id": book.url+"/"+book.collection+"/"+parent+"/sequence/normal",
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
		book.num_of_pages, book.output_folder = extractor.extract_pages(pdf_file,parent)
		print(book.num_of_pages)
		extractor.loop_pages(parent, starter_iiif, book.title, book.issued_date, output_folder)
		book.write_book_node_line(parent)
		book.cleanup_ppms(output_folder)
		print(book.num_of_pages)
		