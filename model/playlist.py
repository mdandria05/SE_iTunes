from dataclasses import dataclass
@dataclass
class Playlist:
    playlist_id: int
    track_id: int
    album_id: int

    def __eq__(self, other):
        return isinstance(other, Playlist) and self.playlist_id == other.playlist_id and self.album_id != other.album_id