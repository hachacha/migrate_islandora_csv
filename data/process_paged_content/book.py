from const import Const
from os import remove

# bulk of variables here
class Book(Const):
	def __init__(self):
		super().__init__()
		# paged constants for descriptions etc.
		self.title = ""
		self.subtitle=""
		self.description = "" 
		self.extent = "" # should be num_of_pages;type
		self.issued_date = ""
		self.subjects = ""
		self.author = ""
		self.publisher=""
		self.doi=""
		self.geo_location = ""
		self.file = ""
		self.copyright = ""
		self.num_of_pages=0
		# open node file and write first line
		self.output_book_nodes_csv = open(self.collection + '_book_nodes.csv','a')
		self.output_book_nodes_csv.write(self.book_node_header)
		
	def write_book_node_line(self,parent):
		print("writing a book line")
		# book_line = ("%s|Thistle year book for %s||%s|%s pages;book|%s-01-01T00:00:00|College Yearbooks|Carnegie-Mellon University|Carnegie-Mellon University|%s_thistle\n") % (self.title,year,collection,str(num_of_pages),year,year)
		# only issue with this is the pages; book for extent... not sure how to tackle this will be specific for each thing
		book_line = ("%s|%s||%s|%s|%s pages; book|%s|%s|%s|%s|%s\n") % (self.title,self.subtitle,self.collection,self.copyright,self.num_of_pages,self.issued_date,self.subjects,self.publisher,self.geo_location,parent)
		self.output_book_nodes_csv.write(book_line)
		self.output_book_nodes_csv.close()

	def cleanup_ppms(self,output_folder):
		remove(output_folder+"/*.ppm")