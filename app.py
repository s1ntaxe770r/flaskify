from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, AUDIO 

app = Flask(__name__)

audio  = UploadSet('audio',AUDIO)
app.config['UPLOADED_AUDIO_DEST'] = 'static/songs'
configure_uploads(app,audio)

@app.route('/')
def index():
    return render_template('landing.html')


@app.route('/listen')
def listen():
    return 'music route'


@app.route('/update',methods=['GET','POST'])
def update():
	if request.method == 'POST' and 'audio' in request.files:
		filename = audio.save(request.files['audio'])
		return filename + 'has been added to the library'
	return render_template('upload.html')

if __name__ == '__main__':
	app.run(debug=True)