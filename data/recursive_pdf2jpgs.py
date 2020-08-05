#/bin/bash
#pip install pdf2image
import os
from pdf2image import convert_from_path

# assumes that all pdfs are in this dir and labeled as TYB_1982_0001.pdf
files = os.listdir('.')

for file in files:
        if file[len(file)-3:len(file)] == 'pdf': # only continue if file is pdf
                year = file[4:8] # get year
                print(year)
                pages = convert_from_path('./'+file, 125, './') # figure out pages
                print("doing it")

                pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)

                index = 1
                for page in pages:
                    print(page._size) # page size should be gleaned and saved
                    page_size = page._size
                    page.save('./images/thistle_'+year+'_page_'+str(index)+'.jpg', 'JPEG')
                    index+=1
                    # exit()

                print("there you go, baby")

        else:
                continue

