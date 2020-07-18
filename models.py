# from flask_sqlalchemy import SQLAlchemy
# from main import app 
# # database config
# project_dir = os.path.dirname(os.path.abspath(__file__))
# db_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))
# app.config['SQLALCHEMY_DATABASE_URI']=db_file
# db = SQLAlchemy(app)

# this file will be unused till i figure out how to import the models into main.py 
  

# class Track(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     track_title = db.Column(db.String(30), nullable=False)
#     track_artist = db.Column(db.String(30), nullable=False)
#     track_location = db.Column(db.String(30), nullable=False)
#     track_duration = db.Column(db.Integer, nullable=False)
