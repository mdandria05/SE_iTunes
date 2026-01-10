from dataclasses import dataclass
@dataclass
class Album:
    id: int
    title: str
    artist_id: int

    def __eq__(self, other):
        return isinstance(other, Album) and self.id == other.id
    def __str__(self):
        return f"{self.title}"
    def __hash__(self):
        return hash(self.id)