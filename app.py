from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, AUDIO
import os

app = Flask(__name__)

audio = UploadSet('audio', AUDIO)
app.config['UPLOADED_AUDIO_DEST'] = 'static/songs'
configure_uploads(app, audio)


@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/listen',methods=['GET'])
def listen():
	if request.method == 'GET':
		path = os.getcwd() + r"\static\songs"
		directory =  os.listdir(path)
		tracks = os.listdir(path)
	return render_template('listen.html',directory=directory,path=path)



@app.route('/update',methods=['GET','POST'])
def update():
	if request.method == 'POST' and 'audio' in request.files:
		filename = audio.save(request.files['audio'])
		return filename + " " + 'has been added to the library'
	return render_template('upload.html')


# TODO: add search feature


if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
