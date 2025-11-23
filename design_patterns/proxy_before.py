# ==============================================
# Before Pattern: Proxy
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how images are loaded and displayed BEFORE applying
#   the Proxy pattern. Every Image loads its heavy data immediately,
#   even if the client never displays it. This wastes time and memory
#   when many images exist but only a few are used.
# ==============================================


# -----------------------------
# Heavy Image Class (No Proxy)
# -----------------------------
# This class simulates the expensive operation of loading
# a large image file into memory.
# -----------------------------
class Image:
    def __init__(self, filename):
        self.filename = filename
        self._load_image_from_disk()

    def _load_image_from_disk(self):
        print(f"Loading '{self.filename}' from disk... (heavy operation)")
        self.data = f"[IMAGE_DATA:{self.filename}]"  # imagine large bitmap data

    def display(self):
        print(f"Displaying image: {self.filename}")


# -----------------------------
# Example usage (Before Proxy)
# -----------------------------
# NOTE:
#   Even though we only display ONE image, THREE images are loaded.
#   The client pays the cost immediately for all images, even unused ones.
# -----------------------------
if __name__ == "__main__":
    print("--- Before Proxy Pattern Example ---\n")

    image1 = Image("big_picture_1.png")
    image2 = Image("big_picture_2.png")
    image3 = Image("big_picture_3.png")

    # Only display one of them
    image2.display()

    print(
        "\nProblem: All images load their heavy data at creation time, even if\n"
        "some are never displayed. This slows down the application when\n"
        "many large files exist. Proxy solves this with lazy loading."
    )


# -----------------------------
# Example Output
# -----------------------------
# --- Before Proxy Pattern Example ---
# Loading 'big_picture_1.png' from disk... (heavy operation)
# Loading 'big_picture_2.png' from disk... (heavy operation)
# Loading 'big_picture_3.png' from disk... (heavy operation)
# Displaying image: big_picture_2.png
#
# Problem: All images load immediately, even unused ones.
#
# ==============================================
# History
# ==============================================
# Before the Proxy pattern (GoF 1994), applications frequently created
# heavy objects directly, causing unnecessary resource usage. The Proxy
# pattern allows delaying creation, controlling access, and adding
# additional behavior, making it widely used in virtual proxies,
# remote proxies, and caching layers.
# ==============================================
