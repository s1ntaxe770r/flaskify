from flask import Flask, render_template, request, flash
from flask_uploads import UploadSet, configure_uploads, AUDIO,UploadNotAllowed
import os

app = Flask(__name__) 

audio = UploadSet("audio", AUDIO)
app.config["UPLOADED_AUDIO_DEST"] = "static/songs"
configure_uploads(app, audio)
app.config["SECRET_KEY"] = "'`-qR49d-7w7}FMRIrjAoenyhhxDXF)*2ycRmkxDx'"
sep = os.path.sep
path = os.getcwd() + os.path.join(sep, "static"+sep,"songs")

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
            print("songs dir not found")
            os.mkdir(path)
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
    app.run(host="0.0.0.0", debug=True, port=3000)
