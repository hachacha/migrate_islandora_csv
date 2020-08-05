from const import Const
import json
from urllib import parse

class Page(Const):
	def __init__(self):
		super().__init__() # will inherrit all const variables. 
		self.page_parent =""
		self.page_description = ""
		self.page_weight = ""
		self.page_file_title = ""
		self.page_file_subtitle = ""
		self.page_file_description = ""
		self.output_page_nodes_csv = open(self.collection + '_page_nodes.csv','w')
		self.output_page_files_csv = open(self.collection + '_page_files.csv','w')
		self.output_page_files_csv.write(self.page_file_header)
		self.output_page_nodes_csv.write(self.page_node_header)

	def increment_page_num(self):
		self.page_num+=1

	def write_page_line(self,title,page_num,parent,issued):
		# node_line = ("Thistle %s page %s|||%s_thistle|%s-01-01T00:00:00|%s|%s/thistle_%s_page_%s.jpg\n") % (year,page_num,year,year,page_num,year,year,page_num)
		#file resides at parent/page_#.jpg
		node_line = ("%s page %s|||%s|%s|%s|%s/page_%s.jpg\n") % (title, page_num,parent,issued,page_num,parent,page_num)
		self.output_page_nodes_csv.write(node_line)

		file_line = ("%s page %s|||%s|%s/page_%s.jpg\n") % (title, page_num,issued,parent,page_num)
		self.output_page_files_csv.write(file_line)
