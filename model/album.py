from dataclasses import dataclass
@dataclass
class Album:
    id: int
    title: str
    artist_id: int
    minuti: float

    def __eq__(self, other):
        return isinstance(other, Album) and self.id == other.id
    def __str__(self):
        return f"{self.title}"
    def __hash__(self):
        return hash(self.id)
    def __lt__(self, other):
        return self.minuti < other.minuti