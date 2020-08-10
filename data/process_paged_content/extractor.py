import json
from pdf2image import convert_from_path
from urllib import parse
from const import Const
from page import Page

class Extractor(Const):
	def __init__(self):
		super().__init__()
		self.images=[]

	def loop_pages(self,parent, starter_iiif, title, issued, output_folder):

		for page_num, page in enumerate(self.images):
			p = Page()
			page_size = page._size
			# to prevent page = 0 
			page_num = page_num+1
			page_num = str(page_num)
			page.save(output_folder+'/page_'+page_num+'.jpg', 'JPEG')
			
			p.write_page_line(title,page_num,parent,issued)

			# details for iiif
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

			print("did page %s" % (page_num))
		print("finished book")
		iiif_json = json.dumps(starter_iiif)
		output_iiif_manifest = open(parent+'.json','w')
		output_iiif_manifest.write(iiif_json)
		output_iiif_manifest.close()


	def extract_pages(self, pdf_file,parent):
			# image extraction, text extraction, page size should be done in extractor
			# values returned here so each page is written in a function and not looped here 
			# loop happens outside this!
			# will take a sec
			output_folder = self.create_image_output_folder(parent)
			self.images = convert_from_path(pdf_file, self.dpi, output_folder)
			return len(self.images), output_folder

			