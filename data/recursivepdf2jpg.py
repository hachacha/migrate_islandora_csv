#/bin/bash
#pip install pdf2image
import os
from pdf2image import convert_from_path

files = os.listdir('.')

for file in files:
        if file[len(file)-3:len(file)] == 'pdf':
                year = file[4:8]
                print(year)
                pages = convert_from_path('./'+file, 125, './')
                print("doing it")
                # make the folder for the year/title if it doesn't exist
                if not os.path.exists('./images/'+str(year)):
                    os.mkdir('./images/'+str(year))
                index = 1
                # save the images
                for page in pages:
                    page.save('./images/'+year+'/thistle_'+year+'_page_'+str(index)+'.jpg', 'JPEG')
                    index+=1

                print("there you go, baby")

        else:
                continue
