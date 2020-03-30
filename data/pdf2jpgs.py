#/bin/bash
#pip install pdf2image

from pdf2image import convert_from_path
pages = convert_from_path('./TYB_1982_0001.pdf', 125, '/home/jon/repos/pdf_to_jpgs')

#pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)

index = 1 
for page in pages:
    page.save('page_'+str(index)+'.jpg', 'JPEG')
    index+=1

print("there you go baby")
