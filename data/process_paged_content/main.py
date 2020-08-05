#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# main

import os
import csv
from urllib import parse
from const import Const, Page, Book


# make me a const and all this
c = Const()


# read from csv
with open('thistle_yearbooks_test.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	line_count = 0
	for row in csv_reader:

		# build book
		book = Book()
		book.title = row['<mods:title>']
		book.subtitle=row['subtitle']
		book.description = row['description'] 
		# self.extent = "" # should be num_of_pages;type
		book.issued_date = row['<mods:dateCreated>']
		book.subjects = row['<mods:subject>']
		book.publisher = row['<mods:publisher>']
		book.geo_location = row['<mods:physicalLocation>']
		book.doi = row['<mods:identifier type="doi">']


		
		# find the file name in the csv and then extract the images
		# should use pdfminer object - layout_scanner 
		# to do both image extraction and text
		pdf_file = 'pdfs/%s/%s' % ( book.collection, row['filename'] )
		print(pdf_file)
		parent = book.title.lower().replace(" ","_")
		starter_iiif = {
                "@type": "sc:Manifest",
                "@id": book.url+"/"+book.collection+"/"+parent+"/manifest",
                "label": "IIIF Manifest",
                "@context": "http://iiif.io/api/presentation/2/context.json",
                "sequences":[{
                    "@context": "http://iiif.io/api/presentation/2/context.json",
                    "@id": book.url+"/"+book.collection+"/"+parent+"/sequence/normal",
                    "@type": "sc:Sequence",
                    "canvases":[]
                }]
            }
		
		
		page = Page()
		num_of_pages = page.loop_pages(pdf_file, parent, starter_iiif, book.title, book.issued_date)
		book.num_of_pages = str(num_of_pages)
		book.write_book_nodes(parent)
		