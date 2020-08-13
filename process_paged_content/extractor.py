from pdf2image import convert_from_path
from const import Const
from page import Page

class Extractor(Const):
	def __init__(self):
		super().__init__()
		self.images=[]


	def extract_pages(self, pdf_file,parent):
			# image extraction, text extraction, page size should be done in extractor
			# values returned here so each page is written in a function and not looped here 
			# loop happens outside this!
			# will take a sec
			output_folder = self.create_image_output_folder(parent)
			self.images = convert_from_path(pdf_file, self.dpi, output_folder)
			return output_folder

			