from PIL import Image
from PIL.ExifTags import TAGS
import os
import shutil

image_folder_name = input("Enter your image folder name:")
image_folder_name = image_folder_name.strip()

EXTENSIONS = ['.JPG','.jpg','.JPEG','.jpeg','.png','.PNG']

def get_file_list(root_dir,E):
    file_list = []
    counter = 1
    dirName = 'Collection Images'
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
        
    folder_path = os.getcwd()
    collection_images_path = folder_path + "\\" + 'Collection Images'
     
    for root, directories, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(ext in filename for ext in E): 
                file_list.append(os.path.join(root, filename))
                counter += 1
                
    for file_path in file_list:
        imge_path = (folder_path + file_path)
        shutil.copy(imge_path, collection_images_path)
        image = Image.open(file_path)
        exifdata = image.getexif()
        #print(file_path)
        for tagid in exifdata:   
            tagname = TAGS.get(tagid, tagid)
            value = exifdata.get(tagid)
            print(f"{tagname:25}: {value}")
    return file_list

file_list = get_file_list('./'+ image_folder_name,EXTENSIONS)

 
