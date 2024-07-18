
# A simple Flask app 
# Logic of creating the blockbusters is in blockbusters.py
# html is in normal place for flask projects

from flask import Flask, send_file, render_template, request
import os
import glob

from blockbusters import create_pdf

app = Flask(__name__)

# How to send files https://pythonprogramming.net/flask-send-file-tutorial/
# How to read from textbox https://stackoverflow.com/questions/46990497/flask-use-a-button-to-submit-text-in-a-text-box-a-form

@app.route('/', methods=['POST', 'GET'])
def index():
	# Delete all existing PDF files to save storage
	filelist = glob.glob('*.pdf')
	for filePath in filelist:
		try:
			os.remove(filePath)
		except OSError:
			print("Error while deleting file")

	#https://flask.palletsprojects.com/en/2.0.x/quickstart/#accessing-request-data
	if request.method == 'POST':

		text = request.form.get('textbox')
		if text is None or text == '':
			return('You need to enter a number into the textbox!')

		textbox_num = int(text)
		num_pages = textbox_num
		print(num_pages)

		create_pdf(int(num_pages))
		return send_file(f'blockbuster-{num_pages}-pages.pdf', download_name=f'blockbuster-{num_pages}-pages.pdf')

	else:
		return render_template('index.html')

@app.route('/file-downloads/')
def file_downloads():
	try:
		return render_template('downloads.html')
	except Exception as e:
		return str(e)

# To run this Flask app:
# 1. cd into src directory
# 2. run "flask run"
# 4. Open http://127.0.0.1:5000/
