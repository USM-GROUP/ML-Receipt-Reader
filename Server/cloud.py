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
client = vision.ImageAnnotatorClient()

def processImage(imagePath, filename):
	#file = os.path.abspath('./images/test.png')
	file = os.path.abspath(imagePath)

	with io.open(file, 'rb') as imagefile:
		content = imagefile.read()

	image = types.Image(content=content)


	response = client.text_detection(image=image)
	labels = response.text_annotations
	words = []
	with io.open('./responses/response_' + filename +'.txt','w') as out:
		print(response, file=out)
		print("Receieved")
		out.close()
	height = labels[0].bounding_poly.vertices[3].y
	labels.pop(0)

	max = 0

	heights = []
	for label in labels:
		poly = label.bounding_poly
		heights.append(poly.vertices[3].y-poly.vertices[0].y )

	print("Unsorted heights")
	print(heights)
	heights.sort()
	print("Sorted heights")
	print(heights)
	median = heights[int(len(heights)/2)]
	print("Medians")
	print(median)
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
			lineStr+=ob['word']+' '
		lines[i] = lineStr
		
	clean(lines)


	items = []
	with io.open('./responses/items_' + filename + '.txt','w') as out:
		for l in lines:
			print(l, file=out)
			print(l)
		print()
		for l in lines:
			if re.search("[0-9]{9}.*[0-9]+[.][0-9]{2}.*", l):
				print(l, file=out)
				print(l)
		out.close()