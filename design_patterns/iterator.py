# ==============================================
# Pattern Name: Iterator
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   The Iterator pattern provides a way to access elements of a
#   collection sequentially without revealing how the collection
#   stores its data. Traversal becomes independent of structure.
#
# What Makes It Unique:
#   Iterator decouples traversal from underlying storage, allowing:
#       - multiple independent iterators
#       - flexible traversal strategies
#       - collections to change internally without breaking loops
# ==============================================


# -----------------------------
# Iterator Class
# -----------------------------
# Stores traversal state independently of the collection.
# -----------------------------
class PlaylistIterator:
    def __init__(self, songs_list):
        self.songs = songs_list
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.songs):
            raise StopIteration

        song = self.songs[self.position]
        self.position += 1
        return song


# -----------------------------
# Collection: Playlist
# -----------------------------
# This class hides its internal structure.
# Internally, the playlist may store songs in different formats.
# This implementation supports:
#   - lists, tuples, sets, generators (any iterable)
#   - dictionaries (converted into a sorted list)
#
# NOTE:
#   More complex structures such as trees, databases, API responses,
#   or nested playlists would require extending __iter__() with
#   custom normalization logic.
# -----------------------------
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __iter__(self):
        # Convert internal data to a consistent list for iteration
        if isinstance(self.songs, dict):
            ordered = [self.songs[key] for key in sorted(self.songs.keys())]
        else:
            ordered = list(self.songs)

        return PlaylistIterator(ordered)


# -----------------------------
# Example Usage
# Includes: list, dict, AND mixed-type iterable
# -----------------------------
if __name__ == "__main__":
    print("--- Iterator Pattern Example ---\n")

    # 1) Old format — list of songs
    playlist_list = Playlist(["Song A", "Song B", "Song C"])

    print("Iterating over LIST playlist:")
    for song in playlist_list:
        print("Playing:", song)

    # 2) Dict format — this broke the BEFORE version
    playlist_dict = Playlist({1: "Song A", 2: "Song B", 3: "Song C"})

    print("\nIterating over DICT playlist (no errors now):")
    for song in playlist_dict:
        print("Playing:", song)

    # 3) Mixed-type iterable — works with current implementation
    print("\nIterating over MIXED-TYPE ITERABLE playlist:")
    mixed = (x for x in ["Intro", 123, True, 9.5, "Final Track"])  # generator with mixed types
    playlist_mixed = Playlist(mixed)

    for item in playlist_mixed:
        print("Playing:", item)


# -----------------------------
# Example Output
# -----------------------------
# --- Iterator Pattern Example ---
#
# Iterating over LIST playlist:
# Playing: Song A
# Playing: Song B
# Playing: Song C
#
# Iterating over DICT playlist (no errors now):
# Playing: Song A
# Playing: Song B
# Playing: Song C
#
# Iterating over MIXED-TYPE ITERABLE playlist:
# Playing: Intro
# Playing: 123
# Playing: True
# Playing: 9.5
# Playing: Final Track
#
#
# ==============================================
# History
# ==============================================
# Before the Iterator pattern, collections were traversed
# using manual indexing (lists) or key access (dicts).
# This tightly coupled traversal logic to the collection’s
# internal structure.
#
# The Iterator pattern introduced independent iterator
# objects that maintain traversal state. Collections now
# provide a uniform way to obtain iterators, allowing
# traversal code ("for x in collection") to remain unchanged
# even if the internal storage changes (list → dict → tree).
# ==============================================
