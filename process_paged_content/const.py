#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import parse
import os

# Const will constants relevant for entire collection

class Const:
	def __init__(self):
		# overall consts
		self.collection_csv = "thistle_yearbooks_test.csv"
		self.url = "http://islandora-dev.library.cmu.edu:8000"
		self.url_escaped = parse.quote(self.url, safe='')
		self.file_staging_url = "http://islandora-file-staging.library.cmu.edu"
		self.collection = "thistle"
		self.collection_pretty = "Thistle Yearbooks"
		self.migration_group = "migrate_thistle"
		self.page_num = 1
		self.dpi = 72
		self.image_output_folder = ("../data/images/%s") % (self.collection)
		self.config_csv_output_folder = ("../data/migrations/%s/") % (self.collection)
		
		# define fields you want to see here, modify how book node line 
		# page node line within the write_x_line function in page and book classes
		self.book_node_header = "title|subtitle|description|collection|copyright|extent|issued|subjects|author|geo_location|file\n"

		self.page_node_header = "title|subtitle|description|parent|issued|weight|file\n"
		
		self.page_file_header = 'title|subtitle|description|issued|file\n'

	def create_image_output_folder(self,folder_name):
		# check if folder exists
		fn = os.getcwd()+"/"+self.image_output_folder+"/"+folder_name
		print(os.path.isdir(fn))
		if os.path.isdir(fn) is False:
			os.mkdir(fn)
		# return combined name
		return fn


	

	

	

class Text(Const):
	def __init__(self):
		super().__init__()
		pass	
