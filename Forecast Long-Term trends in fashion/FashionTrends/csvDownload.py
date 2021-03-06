"""
Downloads images using CSVs generated by webscraper.py and saves them in image_dir
"""
import urllib.request
import csv
import os
from urllib.parse import urlparse
import shutil
import glob

image_dir = 'C:/Users/Bhuvanjeet/Desktop/FashionTrends/Image_Data/Chictopia/Parsed/'

#Find images already in folder to prevent redownload
current_images = glob.glob(image_dir + '*.jpg')
with open('dresses.csv', newline='\n') as file:
   reader = csv.reader(file, delimiter=',')
   for row in reader:
      if '\\' not in row[0].split("\'")[1] and image_dir + os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg') not in current_images: #Skip non-ascii characters - ChicTopia just fails to use them as URLs for some reason
         with urllib.request.urlopen(row[0].split("\'")[1]) as response, open(image_dir + os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg'), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            print(os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg'))

#Reupdate found images in case we already downloaded image previously
current_images = glob.glob(image_dir + '*.jpg')
with open('pants.csv', newline='\n') as file:
   reader = csv.reader(file, delimiter=',')
   for row in reader:
      if '\\' not in row[0].split("\'")[1] and image_dir + os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg') not in current_images: #Skip non-ascii characters - ChicTopia just fails to use them as URLs for some reason
         with urllib.request.urlopen(row[0].split("\'")[1]) as response, open(image_dir + os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg'), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            print(os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg'))

#Reupdate found images in case we already downloaded image previously
current_images = glob.glob(image_dir + '*.jpg')
with open('skirts.csv', newline='\n') as file:
   reader = csv.reader(file, delimiter=',')
   for row in reader:
      if '\\' not in row[0].split("\'")[1] and image_dir + os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg') not in current_images: #Skip non-ascii characters - ChicTopia just fails to use them as URLs for some reason
         with urllib.request.urlopen(row[0].split("\'")[1]) as response, open(image_dir + os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg'), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            print(os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg'))

#Reupdate found images in case we already downloaded image previously
current_images = glob.glob(image_dir + '*.jpg')
with open('shirts.csv', newline='\n') as file:
   reader = csv.reader(file, delimiter=',')
   for row in reader:
      if '\\' not in row[0].split("\'")[1] and image_dir + os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg') not in current_images: #Skip non-ascii characters - ChicTopia just fails to use them as URLs for some reason
         with urllib.request.urlopen(row[0].split("\'")[1]) as response, open(image_dir + os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg'), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
            print(os.path.basename(urlparse(row[0].split("\'")[1]).path).replace('.jpg', row[1] + '.jpg'))