# ==============================================
# Pattern Name: Proxy
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Proxy pattern provides a stand-in (or substitute) for another
#   object in order to control access, add behavior, or delay expensive
#   creation. In this example, ImageProxy loads the real image only when
#   it is first displayed — enabling lazy loading.
#
# What Makes It Unique:
#   Proxy exposes the SAME interface as the real object while adding
#   useful functionality such as lazy loading, caching, access control,
#   or logging, without modifying the real class.
# ==============================================


# -----------------------------
# Real Image (Heavy Object)
# -----------------------------
class Image:
    def __init__(self, filename):
        self.filename = filename

    def _load_image_from_disk(self):
        print(f"Loading '{self.filename}' from disk... (heavy operation)")
        self.data = f"[IMAGE_DATA:{self.filename}]"  # simulate heavy data

    def display(self):
        print(f"Displaying image: {self.filename}")


# -----------------------------
# Proxy Image (Lazy Loader)
# -----------------------------
# Loads the real image ONLY when display() is called the first time.
# Subsequent calls do not reload the image.
# -----------------------------
class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None  # real object is not created yet

    def display(self):
        if self._real_image is None:
            print("[Proxy] Real image not loaded yet. Loading now...")
            self._real_image = Image(self.filename)
            self._real_image._load_image_from_disk()
        else:
            print("[Proxy] Using cached image. No reload needed.")

        self._real_image.display()


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Proxy Pattern Example ---\n")

    # Create three proxy images (matching the before-file example)
    image1 = ImageProxy("big_picture_1.png")
    image2 = ImageProxy("big_picture_2.png")
    image3 = ImageProxy("big_picture_3.png")

    # First display triggers loading for ONLY one image
    image2.display()

    print()

    # Second display uses cached data (no reloading)
    image2.display()


# -----------------------------
# Example Output
# -----------------------------
# --- Proxy Pattern Example ---
# [Proxy] Real image not loaded yet. Loading now...
# Loading 'big_picture_2.png' from disk... (heavy operation)
# Displaying image: big_picture_2.png
#
# [Proxy] Using cached image. No reload needed.
# Displaying image: big_picture_2.png
#
#
# ==============================================
# History
# ==============================================
# The Proxy pattern (GoF 1994) emerged to provide controlled access to
# resources — whether they are expensive, remote, sensitive, or cached.
# Common uses today include virtual proxies (lazy loading), remote
# proxies (network objects), protection proxies (security layers), and
# smart proxies (logging or reference counting).
# ==============================================
