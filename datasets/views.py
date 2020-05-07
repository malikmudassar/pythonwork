import csv
import fnmatch
import os
import glob
import sys
import io
import pandas as pd
import re
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from . models import Uploader
from . models import dataSet

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def readfile():
    SourcePath='/home/mudassar/python-apps/env/src/uploads/'
    SrcFiles=glob.glob(SourcePath + '*.csv')
    df=''
    for i in range(0,len(SrcFiles)):
        head, tail = os.path.split(SrcFiles[i])
        
    # if (fnmatch.fnmatch(tail,'*ETHBTC*'+'*Trade*'+'*.csv')):
        with open(head + '/' + tail) as csvfile:
            print('file read...')
            dataFrame = pd.read_csv(head + '/' +tail)
            print('printing dataFrame')
            print(dataFrame['Time'])
            df=dataFrame['Price']
    return HttpResponse(df)

def upload(request):
    if request.method=='GET':
        return render(request, 'home.html', {})
    csv_file=request.FILES['file']
    # return HttpResponse(r)
    # fUpload=Uploader(file=inputFile)
    # fUpload.save()
    data_set=csv_file.read().decode('UTF-8')
    io_String=io.StringIO(data_set)
    next(io_String)
    for column in csv.reader(io_String, delimiter=',', quotechar='|'):
        _, created = dataSet.objects.update_or_create(   
            ds_name='A',        
            pair=column[0],
            time=column[1], 
            _id=column[2],
            price=column[2],
            volume=column[4],
            side=column[5]
        )
    context={}
    return render(request, 'home.html', context)
    # return HttpResponse(io_String)
    # return readfile()
    # return render(request, "home.html", {})

