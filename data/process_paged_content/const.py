#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import parse
from pdf2image import convert_from_path
import json
# Const will constants relevant for entire collection

class Const:
	def __init__(self):
		# overall consts
		self.url = "http://islandora-dev.library.cmu.edu:8000"
		self.url_escaped = parse.quote(self.url, safe='')
		self.remote_url = "http://islandora-file-staging.library.cmu.edu"
		self.collection = "thistle"
		self.collection_pretty = "Thistle Yearbooks"
		self.migration_group = "migrate_thistle"
		self.page_num = 1

# bulk of variables here
class Book(Const):
	def __init__(self):
		super().__init__()
		# paged constants for descriptions etc.
		self.title = ""
		self.subtitle=""
		self.description = "" 
		# self.extent = "" # should be num_of_pages;type
		self.issued_date = ""
		self.subjects = ""
		self.author = ""
		self.publisher=""
		self.doi=""
		self.geo_location = ""
		self.file = ""
		self.num_of_pages=0
		self.output_book_nodes_csv = open(self.collection + '_book_nodes.csv','w')
		self.output_book_nodes_csv.write('title|subtitle|description|collection|extent|issued|subjects|author|geo_location|file\n')

class Text(Const):
	def __init__(self):
		super().__init__()
		pass	

class Page(Const):
	def __init__(self):
		super().__init__() # will inherrit all const variables. 
		self.page_parent =""
		self.page_description = ""
		self.page_weight = ""
		self.page_file_title = ""
		self.page_file_subtitle = ""
		self.page_file_description = ""
		self.output_page_files_csv = open(self.collection + '_page_files.csv','w')
		self.output_page_files_csv.write('title|subtitle|description|issued|file\n')
		self.output_page_nodes_csv = open(self.collection + '_page_nodes.csv','w')
		self.output_page_nodes_csv.write('title|subtitle|description|parent|issued|weight|file\n')

	def increment_page_num(self):
		self.page_num+=1

	def loop_pages(self, pdf_file, parent, starter_iiif, title, issued):
		# image extraction, text extraction, page size should be done in extractor
		# values returned here so each page is written in a function and not looped here 
		# loop happens outside this!
		# will take a sec
		
		print(starter_iiif)
		images = convert_from_path(pdf_file, 125, './')
		num_of_pages = len(images)
		for page_num, page in enumerate(images):
			page_size = page._size
			page_num = str(page_num)
			# node_line = ("Thistle %s page %s|||%s_thistle|%s-01-01T00:00:00|%s|%s/thistle_%s_page_%s.jpg\n") % (year,page_num,year,year,page_num,year,year,page_num)
			#file resides at parent/page_#.jpg
			node_line = ("%s page %s|||%s|%s|%s|%s/page_%s.jpg\n") % (title, page_num,parent,issued,page_num,parent,page_num)
			self.output_page_nodes_csv.write(node_line)

			file_line = ("%s page %s|||%s|%s/page_%s.jpg\n") % (title, page_num,issued,parent,page_num)
			self.output_page_files_csv.write(file_line)
			# label for page
			label = self.collection+"_"+parent+"_page_"+page_num+".jpg"
			url_encoded_label = parse.quote(label, safe='')
			# manifest id and "on"
			canvas_id = self.url+"/"+self.collection+"/"+parent+"/canvas/"+page_num
			# based on what's already in islandora node/x/manifest
			page_dict = {

				"@id": canvas_id,
				"@type": "sc:Canvas",
				"label": label,
				"height": page_size[0],
				"width": page_size[1],
				"images": [
				{
					"@id": self.url+"/"+self.collection+"/"+parent+"/annotation/"+page_num,
					"@type": "oa:Annotation",
					"motivation": "sc:painting",
					"resource": {
						"@id": self.url+"/cantaloupe/iiif/2/"+self.url_escaped+"%2F_flysystem%2Ffedora%2F"+self.migration_group+"%2F"+url_encoded_label+"/full/full/0/default.jpg",
						"@type": "dctypes:Image",
						"format": "image/jpeg",
						"height": page_size[0],
						"width": page_size[1],
						"service": {
							"@id": self.url+"/cantaloupe/iiif/2/"+self.url_escaped+"%2F_flysystem%2Ffedora%2F"+self.migration_group+"%2F"+url_encoded_label,
							"@context": "http://iiif.io/api/image/2/context.json",
							"profile": "http://iiif.io/api/image/2/profiles/level2.json"
						}
					},
					"on": canvas_id
				}
				]
			}
			starter_iiif['sequences'][0]['canvases'].append(page_dict)

			print("done did a page")
		print("finished book")
		iiif_json = json.dumps(starter_iiif)
		output_iiif_manifest = open(parent+'.json','w')
		output_iiif_manifest.write(iiif_json)
		output_iiif_manifest.close()
		return num_of_pages