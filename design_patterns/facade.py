# ==============================================
# Pattern Name: Facade
# Pattern Type: Structural
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
# Description:
#   The Facade pattern provides a simplified, high-level interface
#   to a set of complex subsystems. It hides the internal steps and
#   dependencies required to perform an operation, making the client
#   code cleaner and easier to use.
#
# What Makes It Unique:
#   Facade unifies many subsystem calls into ONE straightforward method.
#   It reduces complexity while keeping the subsystem classes unchanged.
# ==============================================


# -----------------------------
# Subsystem: Canvas
# -----------------------------
# Handles low-level drawing operations.
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
# Facade Class
# -----------------------------
# Provides ONE method that hides all the internal drawing steps.
# -----------------------------
class DrawingFacade:
    def __init__(self):
        self.canvas = Canvas()
        self.brush = Brush()
        self.color = ColorManager()
        self.layers = LayerManager()

    def draw_circle(self, x, y, radius, color="black", brush_size=2):
        print("--- Using Drawing Facade ---")
        self.layers.select_layer("main")
        self.color.set_color(color)
        self.brush.set_size(brush_size)
        self.canvas.move_to(x, y)
        self.canvas.draw_circle(radius)
        self.canvas.apply()
        self.layers.merge()


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    print("--- Facade Pattern Example ---\n")

    facade = DrawingFacade()

    # Client calls ONE simple method
    facade.draw_circle(10, 20, 5, color="red", brush_size=3)


# -----------------------------
# Example Output
# -----------------------------
# --- Facade Pattern Example ---
# --- Using Drawing Facade ---
# LayerManager: selecting layer 'main'
# ColorManager: setting color to red
# Brush: setting size to 3
# Canvas: moving cursor to (10, 20)
# Canvas: drawing circle with radius 5
# Canvas: applying drawing operations to surface
# LayerManager: merging layers
#
# ==============================================
# History
# ==============================================
# The Facade pattern was introduced in the GoF book (1994) to simplify the
# interaction with complex subsystems. It helps reduce coupling by exposing
# a single, easy-to-use interface while keeping the underlying subsystem
# intact and flexible.
# ==============================================
