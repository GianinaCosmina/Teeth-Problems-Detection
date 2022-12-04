# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:39:54 2021

@author: serdarhelli
"""

import requests
from zipfile import ZipFile
from io import BytesIO

def download_dataset(save_path):
    r = requests.get("https://data.mendeley.com/public-files/datasets/hxt48yk462/files/c2df1e1e-9939-4197-9bac-1eb697a64094/file_downloaded")
    print("Downloading...")
    z = ZipFile(BytesIO(r.content))    
    z.extractall(save_path)
    print("Completed...")
