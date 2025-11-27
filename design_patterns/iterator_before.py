# ==============================================
# BEFORE — Iterator Pattern
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Before the Iterator pattern existed, collections exposed their
#   internal structure directly. Looping through items required:
#       - manual indexing
#       - while loops
#       - knowing exactly how data was stored
#
#   This made traversal tightly coupled to internal details.
#   If the collection changed (e.g., from list → dict),
#   all traversal logic had to be rewritten.
# ==============================================


# -----------------------------
# BEFORE: Manual Playlist implementation
# -----------------------------
class Playlist:
    def __init__(self, songs):
        self.songs = songs  # stored as a list

    def get_song_count(self):
        return len(self.songs)

    def get_song_at(self, index):
        return self.songs[index]


# -----------------------------
# BEFORE: Manual traversal (tightly coupled)
# -----------------------------
def play_all_songs(playlist: Playlist):
    index = 0
    count = playlist.get_song_count()

    # Manual, low-level iteration
    while index < count:
        song = playlist.get_song_at(index)
        print(f"Playing: {song}")
        index += 1


# -----------------------------
# Example Usage 1 (works)
# -----------------------------
if __name__ == "__main__":
    print("--- BEFORE Iterator Example (List Format) ---\n")

    playlist = Playlist(["Song A", "Song B", "Song C"])
    play_all_songs(playlist)


# -----------------------------
# Example Usage 2 (FAILS when internal structure changes)
# -----------------------------
# Now imagine the playlist changes its internal format:
#
# NEW FORMAT:
#     {
#         1: "Song A",
#         2: "Song B",
#         3: "Song C"
#     }
#
# With the BEFORE logic, play_all_songs() will break.
# Why?  
#   - get_song_count() → returns number of keys
#   - get_song_at(index) → tries dict[index]
#   - dict keys are 1, 2, 3 but index starts at 0
#
# This demonstrates how fragile manual iteration is.
# -----------------------------

    print("\n--- BEFORE Iterator Example (Dict Format — Expected Failure) ---\n")

    new_format = {1: "Song A", 2: "Song B", 3: "Song C"}  # changed storage
    broken_playlist = Playlist(new_format)

    try:
        play_all_songs(broken_playlist)
    except Exception as e:
        print("ERROR while playing songs (as expected):")
        print("   ", e)


# -----------------------------
# Example Output
# -----------------------------
# --- BEFORE Iterator Example (List Format) ---
#
# Playing: Song A
# Playing: Song B
# Playing: Song C
#
# --- BEFORE Iterator Example (Dict Format — Expected Failure) ---
#
# ERROR while playing songs (as expected):
#    'dict' object is not subscriptable by index 0
#
#
# ==============================================
# History
# ==============================================
# Before the Iterator pattern, collections were traversed using
# manual index-based loops. This made code dependent on how data
# was stored internally. Changing the structure (list → dict →
# tree) required rewriting all traversal logic everywhere.
#
# The Iterator pattern separated traversal from structure by
# introducing iterator objects that maintain their own traversal
# state. This allowed:
#   - hiding internal data structure
#   - multiple simultaneous iterators
#   - flexible traversal strategies (forward, reverse, filtered)
# ==============================================
