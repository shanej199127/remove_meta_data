# -*- coding: utf-8 -*-
"""
Created on 01_05_2019

@author: Shanaka Jayatilake (v2)

purpose: automatically remove meta data from any sorted image before
being uploaded to aws or azure or feeding to the network.

** run this inside the images or sorted_images directory

"""
import os
import os.path
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

#get current working folder --Decomment if the images are in your working directory
#root_folder = os.getcwd()

#prompt the user to enter the name of the file in the same directory
print("This script is used to remove meta data of images inside image folder and sorted_images folder. The path should be with the correct folder..")
print("Please enter root folder path as root..\(images or sorted images) ")
root_folder = input()

#build the paths of each file within the subfolders
paths_of_files = []
#get root, directory and files 
for root, direc, files in os.walk(root_folder):
   
    for file in files:
        #if '.jpg' in file:# --- sometimes all the images would not be jpg
        paths_of_files.append(os.path.join(root, file))
        
#if needed to skip an image 
skip_number=input("If needed to run from the middle enter the image number to skip:")
skip_number=int(skip_number,10)


#remove metadata for each file in the paths_of_files array     
if skip_number > 0:
    del paths_of_files[0 : skip_number] 

for i, f in enumerate(paths_of_files):
    #open image
    image = Image.open(f)
    image_removed = image.convert('RGB') #convert RGBA(PNG) to jpeg images only with RGB
    
    
    # deletes exif data or meta data 
    data = list(image_removed.getdata())
    image_without_exif = Image.new(image_removed.mode, image_removed.size)
    image_without_exif.putdata(data)
    
    #resave the jpg in another folder under meta data removed    
    image_without_exif.save(f)    
    #move to a done folder 
    new_file_path =os.path.join(root, file)
    
    print ("Removing metadata --> {:d}th image".format(i+skip_number))
    
    

print ("All Metadata are removed in --> {:d} images".format(len(paths_of_files)))
