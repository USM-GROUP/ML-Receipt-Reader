import io
import os
import json
import re
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./config/vision_config.json"

def clean(arr):
    while '' in arr:
        arr.remove('')

def removeKeywords(arr):
    keywords = ['TOTAL','COUPON','DISCOUNT', 'TAX', 'DEBIT', 'CREDIT', 'CHANGE']
    remove = []
    for i in arr:
        for k in keywords:
            if k in i:
                remove.append(i)
                break

    for r in remove:
        arr.remove(r)

def lineDetection(label):
    height = labels[0].bounding_poly.vertices[3].y
    labels.pop(0)
    heights = []
    for label in labels:
        poly = label.bounding_poly
        heights.append(poly.vertices[3].y-poly.vertices[0].y )

    #print(heights)
    heights.sort()
    #print(heights)
    median = heights[int(len(heights)/2)]
    #print(median)
    size = int(height/median) +1
    lines = []
    for i in range(0,size):
        lines.append([])
    for label in labels:
        vert = label.bounding_poly.vertices[3]
        line = int(vert.y/median)
        lines[line].append({'word':label.description,'x':vert.x})

    for i in range(0,len(lines)):
        line = lines[i]
        line = sorted(line, key = lambda i: i['x'])
        lineStr = ''
        for ob in line:
            lineStr+=ob['word'].upper()+' '
        lines[i] = lineStr
        
    clean(lines)

client = vision.ImageAnnotatorClient()

file = os.path.abspath('resources/test.jpg')

with io.open(file, 'rb') as imagefile:
    content = imagefile.read()

image = types.Image(content=content)


response = client.text_detection(image=image)
labels = response.text_annotations
words = []
with io.open('responded.txt','w') as out:
    print(response, file=out)
    print("Receieved")




items = []

for l in lines:
        if re.search("[0-9]+[.][0-9]{2}.*", l):
            items.append(l)

removeKeywords(items)

with io.open('items.txt','w') as out:
    print(items)
    
    