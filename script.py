from tinytag import TinyTag


class TrackInfo:
    """ returns a dictionary of audio metadata  
    Dictonary keys : title , artist,track_lenght"""
    def All(song):
        tag = TinyTag.get(song)
        title = tag.title
        artist = tag.artist
        track_lenght = tag.duration

        results = {
            "title": title,
            "artist": artist,
            "track_lenght": track_lenght
        }

        return results
