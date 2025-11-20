# ==============================================
# Before Pattern: Facade
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   Demonstrates how drawing a simple shape required interacting with
#   multiple low-level subsystem classes BEFORE introducing the Facade.
#   The client must manually coordinate Canvas, Brush, ColorManager,
#   and LayerManager in the correct order.
#   This leads to verbose, error‑prone, and hard‑to‑maintain code.
# ==============================================


# -----------------------------
# Subsystem: Canvas
# -----------------------------
class Canvas:
    def move_to(self, x, y):
        print(f"Canvas: moving cursor to ({x}, {y})")

    def draw_circle(self, radius):
        print(f"Canvas: drawing circle with radius {radius}")

    def apply(self):
        print("Canvas: applying drawing operations to surface")


# -----------------------------
# Subsystem: Brush
# -----------------------------
class Brush:
    def set_size(self, size):
        print(f"Brush: setting size to {size}")


# -----------------------------
# Subsystem: Color Manager
# -----------------------------
class ColorManager:
    def set_color(self, color):
        print(f"ColorManager: setting color to {color}")


# -----------------------------
# Subsystem: Layer Manager
# -----------------------------
class LayerManager:
    def select_layer(self, name):
        print(f"LayerManager: selecting layer '{name}'")

    def merge(self):
        print("LayerManager: merging layers")


# -----------------------------
# Example usage (Before Facade)
# -----------------------------
# NOTE:
#   To draw a simple circle, the client must:
#   - select layer
#   - choose color
#   - set brush size
#   - move canvas cursor
#   - draw circle
#   - apply drawing
#   - merge layers
#   All steps must be performed in the correct order.
# -----------------------------
if __name__ == "__main__":
    print("--- Before Facade Pattern Example ---\n")

    canvas = Canvas()
    brush = Brush()
    color = ColorManager()
    layers = LayerManager()

    layers.select_layer("main")
    color.set_color("red")
    brush.set_size(3)
    canvas.move_to(10, 20)
    canvas.draw_circle(5)
    canvas.apply()
    layers.merge()

    print(
        "\nEven a simple drawing requires many subsystem calls.\n"
        "Adding new drawing steps or changing order requires updating\n"
        "every place where drawing occurs. This is error‑prone and complex."
    )


# -----------------------------
# Example Output
# -----------------------------
# --- Before Facade Pattern Example ---
# LayerManager: selecting layer 'main'
# ColorManager: setting color to red
# Brush: setting size to 3
# Canvas: moving cursor to (10, 20)
# Canvas: drawing circle with radius 5
# Canvas: applying drawing operations to surface
# LayerManager: merging layers
#
# Even a simple drawing requires many subsystem calls.
# ==============================================
# History
# ==============================================
# Before the Facade pattern (GoF 1994), client code frequently had to manage
# complex subsystems directly. This created tight coupling and duplicated
# sequences of operations. Facade introduced a single high‑level interface
# to simplify usage and hide subsystem complexity.
# ==============================================
