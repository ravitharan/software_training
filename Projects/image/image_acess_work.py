from PIL import Image
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
import os
import shutil
from matplotlib import pyplot

image_folder_name = input("Enter your image folder name:")
image_folder_name = image_folder_name.strip()

EXTENSIONS = ['.JPG','.jpg','.JPEG','.jpeg','.png','.PNG']

def get_file_list(root_dir,E):
    
    file_list = []
    counter = 1
    New_folder = 'Collection Images'
    try:
        # Create target Directory
        os.mkdir(New_folder)
        print("Directory " , New_folder ,  " Created ") 
    except FileExistsError:
        print("Directory " , New_folder ,  " already exists")
        
    folder_path = os.getcwd()
    collection_images_path = folder_path + "\\" + 'Collection Images'
     
    for root, directories, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(ext in filename for ext in E): 
                file_list.append(os.path.join(root, filename))
                counter += 1
                
    for file_path in file_list:
        image = Image.open(file_path)
        
        width,height = image.size
        new_width = (width//2)
        new_height = (height//2)
        resized_image = image.resize((new_width,new_height))
        
        file_path = file_path.replace("./","")
        file_path = (os.path.split(file_path)[-1])
        imge_path = (collection_images_path + "\\" + file_path)
        resized_image.save(imge_path,quality = 45)
        
        exifdata = image.getexif()
        if exifdata is None:
            print('Sorry, image has no exif data.') 
        else:
            print("yes............................................................")
            for key, value in exifdata.items():
                if key in ExifTags.TAGS:
                    print(f'{ExifTags.TAGS[key]}:{value}')
             
    return file_list , New_folder

file_list,New_folder = get_file_list('./'+ image_folder_name,EXTENSIONS)
