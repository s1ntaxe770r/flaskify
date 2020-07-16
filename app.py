
from flask_uploads import UploadSet, configure_uploads, AUDIO,UploadNotAllowed
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy 
from script import TrackInfo
from models import Track

import os


app = Flask(__name__) 

audio = UploadSet("audio", AUDIO)
app.config["UPLOADED_AUDIO_DEST"] = "static/songs"
configure_uploads(app, audio)
app.config["SECRET_KEY"] = "`-qR49d-7w7}FMRIrjAoenyhhxDXF)*2ycRmkxDx"
sep = os.path.sep
path = os.getcwd() + os.path.join(sep, "static"+sep,"songs")

# database config
project_dir = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))
app.config['SQLALCHEMY_DATABASE_URI']=db_file
db = SQLAlchemy(app)



@app.route("/")
def index():
    return render_template("landing.html")


@app.route("/listen", methods=["GET"])
def listen():
    if request.method == "GET":
        try:
            directory = os.listdir(path)
            tracks = os.listdir(path)
        except FileNotFoundError as err:
            raise err 
           
    return render_template("listen.html", directory=directory)

@app.route("/update", methods=["GET", "POST"])
def update(request):
    if request.method == "POST" and "audio" in request.files:
        try:
            filename = audio.save(request.files["audio"])
            return filename + " " + "has been added to the library"
        except UploadNotAllowed as err:
            return '<h1>sorry file type is not allowed :( </h1>', 406
      
       
    return render_template("upload.html")


# TODO: add search feature

# def delete(filename):
#     for song in os.listdir(path):
#         if song == filename:
#             location = path+sep+filename
#             os.remove(location)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
