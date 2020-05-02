#!/usr/bin/python
import os
import cloud
from bottle import route, run, template, request, post, get,response

@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

@route('/upload', method='POST')
def do_upload():
	category   = request.forms.get('category')
	upload     = request.files.get('photo')
	print('Received file [' + upload.filename + ']')
	name, ext = os.path.splitext(upload.filename)
	if ext not in ('.png','.jpg','.jpeg'):
		return 'File extension not allowed.'
	print('Extension: ' + ext)
	#save_path = get_save_path_for_category(category)
	save_path = './images/' + upload.filename
	#save_path = 'testfile.png'
	print('Saving to ' + save_path)
	upload.save(save_path) # appends upload.filename automatically
	cloud.processImage(save_path, name)
	#print('Removing uneeded image file...')
	#os.remove(save_path)
	response.status = 200
	return 'OK'
	
@route('/api', method='POST')
def upload():
	upload = request.files.get('file')
	print(upload.filename)
	upload.save('out.png')
	
run(host='192.168.0.23', port=8080)