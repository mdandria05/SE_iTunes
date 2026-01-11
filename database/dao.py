from database.DB_connect import DBConnect
from model.album import Album as a
from model.playlist import Playlist as p

class DAO:
    @staticmethod
    def get_albums(minuti:float):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT a.id, a.title, a.artist_id, album_minuti.minuti
                    FROM (SELECT album_id, (SUM(milliseconds)/1000)/60 as minuti
		                    FROM track
		                    GROUP BY album_id) as album_minuti,
                        album as a
                    WHERE a.id = album_minuti.album_id AND album_minuti.minuti > %s"""

        cursor.execute(query,(minuti,))

        for row in cursor:
            result.append(a(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_playlist():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT pt.playlist_id, pt.track_id, t.album_id
                    FROM playlist_track as pt,
	                        track as t
                    WHERE pt.track_id = t.id"""

        cursor.execute(query)

        for row in cursor:
            result.append(p(**row))

        cursor.close()
        conn.close()
        return result