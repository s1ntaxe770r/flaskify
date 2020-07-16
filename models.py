from app import db


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_title = db.Column(db.String(30), nullable=False)
    track_artist = db.Column(db.String(30), nullable=False)
    track_location = db.Column(db.String(30), nullable=False)
    track_duration = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.track_title
